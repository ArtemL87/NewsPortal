from django.db import models

from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=20)

class Author(models.Model):
    user_com = models.OneToOneField('User', on_delete=models.CASCADE)
    rating = models.FloatField(default=2.5)

    def update_rating(self):
        x = 0
        n = self.post_set.all().values('rating')
        for i in range(len(n)):
            x += n[i]['rating']
        rating_news = x * 3

        rating_comment = 0
        n = self.user_com.comment_set.all().values('rating')
        for i in range(len(n)):
            rating_comment += n[i]['rating']

        rating_comments_on_news = 0
        n = self.post_set.all()
        for i in range(len(n)):
            m = n[i].comment_set.all().values('rating')
            for j in range(len(m)):
                rating_comments_on_news += m[j]['rating']

        self.rating = rating_news + rating_comment + rating_comments_on_news
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')


class Post(models.Model):
    news = 'новость'
    article = 'статья'

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    news_article = models.CharField(max_length=20)
    time_in = models.DateTimeField(auto_now_add=True)
    category_com = models.ManyToManyField(to='Category', through='PostCategory', related_name='news')
    title_news = models.CharField(max_length=50)
    text_news = models.TextField()
    rating = models.FloatField(default=2.5)

    def like(self):
        if self.rating < 5.0:
            self.rating += 0.1
            self.save()

    def dislike(self):
        if self.rating > 0.0:
            self.rating -= 0.1
            self.save()

    def preview(self):
        return f'{self.text_news[:124]}...'


    def __str__(self):
        return f'{self.title_news.title()}: {self.text_news}'

    def get_absolute_url(self):
        return f'/post/{self.id}'


class PostCategory(models.Model):
    post_com = models.ForeignKey('Post', on_delete=models.CASCADE)
    category_com = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    post_com = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_com = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.TextField(default='Хорошая новость')
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=2.5)

    def like(self):
        if self.rating < 5.0:
            self.rating += 0.1
            self.save()

    def dislike(self):
        if self.rating > 0.0:
            self.rating -= 0.1
            self.save()


# Create your models here.