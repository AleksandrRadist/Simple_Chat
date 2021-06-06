from django.urls import path
from django.urls import re_path
from .views import ChatDetailView, ChatListView
from .views import MessageCreateView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', ChatListView.as_view(), name='index'),
    path('chats/', ChatListView.as_view(), name='chats'),
    path('chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat'),
    path('create/<int:object_id>/', MessageCreateView.as_view(), name='message_create')
]
