from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'chat_id': self.pk})

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.pk}"

