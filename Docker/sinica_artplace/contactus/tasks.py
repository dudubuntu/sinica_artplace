from celery import shared_task
from django.core.mail import send_mail

from django.conf import settings


@shared_task
def task_send_email(name, phone_number, created_at, *args, **kwargs):
    send_mail(
        subject='[Sinica-artplace] Обратная связь',
        message=f'{name} заказал звонок на номер {phone_number}.\n{created_at}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER])
    return True