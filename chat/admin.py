from django.contrib import admin

from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date',)
    readonly_fields = ('pub_date',)
    empty_value_display = '-пусто-'


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_date',)
    readonly_fields = ('creation_date',)
    empty_value_display = '-пусто-'


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
