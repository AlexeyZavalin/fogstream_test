from django.contrib import admin
from mainapp.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('email',)
