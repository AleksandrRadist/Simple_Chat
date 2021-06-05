from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Chat, Message
from django.http import HttpResponseRedirect
from django.views import View
from .forms import MessageForm
from django.shortcuts import redirect

class ChatListView(ListView):

    model = Chat
    template_name = 'chats.html'
    context_object_name = 'chats'


class ChatDetailView(DetailView):

    model = Chat
    template_name = 'chat.html'
    context_object_name = 'chat'
    pk_url_kwarg = 'chat_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm(self.request.POST or None)
        return context


class MessageCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MessageForm(request.POST or None)
        chat = Chat.objects.get(pk=kwargs['chat_id'])
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.text = form.cleaned_data['text']
            new_comment.save()
            return redirect('chats', chat_id=chat.id)
        messages.add_message(request, messages.ERROR, 'Не удалось отправить сообщение')
        return redirect('chats', chat_id=chat.id)
