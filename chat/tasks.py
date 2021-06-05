from celery import shared_task
from datetime import datetime, timedelta

from .models import Message


@shared_task
def delete_old_messages():
    d = datetime.today() - timedelta(hours=0, minutes=1)
    messages = Message.objects.filter(pub_date__lte=d)
    count = messages.count()
    messages.delete()
    return count
