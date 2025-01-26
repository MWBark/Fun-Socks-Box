from django.contrib import admin
from .models import Message


class MessagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'subject',
    )


admin.site.register(Message, MessagesAdmin)
