from django.contrib import admin
from .models import Author, Post, Category, User, Comment

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title_news', 'author', 'time_in', 'news_article')
    list_filter = ('author', 'time_in')
    search_fields = ('author', 'time_in')

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Comment)
# admin.site.unregister(Post)


# Register your models here.
