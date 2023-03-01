from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
import datetime
from News.models import Post, Category


@shared_task
def new_post(preview, pk, title_news, subscribers):
    html_content = render_to_string(
        'news_created.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/post/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title_news,
        body='',
        from_email='artem.l.1987@yandex.ru',
        to=['lordtemik@gmail.com', ],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def post_week():
    #  Your job processing logic here...
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('category_com__category', flat=True))
    subscribers = set(Category.objects.filter(category__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email='artem.l.1987@yandex.ru',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()