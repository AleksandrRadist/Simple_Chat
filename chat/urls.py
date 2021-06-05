from django.urls import path

from .views import ChatDetailView, ChatListView
from .views import MessageCreateView


urlpatterns = [
    path('chats/', ChatListView.as_view(), name='chats'),
    path('chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat'),
    path('create/<str:content_type>/<int:object_id>/', MessageCreateView.as_view(), name='message_create')
]
