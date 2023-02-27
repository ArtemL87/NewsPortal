from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_admins, EmailMultiAlternatives
from .models import PostCategory, Category
from NewsPortal.settings import SITE_URL


def send_notifications(preview, pk, title_news, subscribers):
    html_content = render_to_string(
        'news_created.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/post/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title_news,
        body='',
        from_email='artem.l.1987@yandex.ru',
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_managers_post(request, sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category_com.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title_news, subscribers)

    mail_admins(
        subject=f'{instance.title_news}',
        message=instance.text_news,
    )
