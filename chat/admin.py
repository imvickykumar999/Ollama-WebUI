from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message', 'timestamp')  # Fields to display in the admin list view
    list_filter = ('sender', 'timestamp')  # Filters to allow filtering by sender or timestamp
    search_fields = ('message',)  # Enable search by message content
    ordering = ('-timestamp',)  # Order messages by latest timestamp first
