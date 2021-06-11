import os
from celery import shared_task
from django.conf import settings

from .models import *


@shared_task
def clear_media(*args, **kwargs):
    q = Item.objects.values_list('poster', 'author_img')
    names = set()
    for item in q:
        names.update(item)
    listdir = set()
    listdir.update(os.listdir(settings.MEDIA_ROOT))
    to_delete = listdir.difference(names)
    for filename in to_delete:
        os.remove(settings.MEDIA_ROOT / filename)

    return True