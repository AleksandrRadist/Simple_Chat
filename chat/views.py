from django.views.generic import ListView, DetailView

from .models import Chat, Message


class ChatListView(ListView):

    model = Chat
    template_name = 'chats.html'
    context_object_name = 'chats'


class ChatDetailView(DetailView):

    model = Chat
    template_name = 'chat.html'
    context_object_name = 'chat'
    pk_url_kwarg = 'chat_id'

