from django.urls import path

from .views import ChatDetailView, ChatListView

urlpatterns = [
    path('chats/', ChatListView.as_view(), name='chats'),
    path('chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat')
]
