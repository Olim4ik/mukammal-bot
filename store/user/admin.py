from django.contrib import admin

from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    """TelegramUser"""
    list_display = ("full_name", "username", "phone_number", "chat_id")
    list_display_links = ("full_name",)
    # readonly_fields = ("created_at", )
    search_fields = ["full_name"]

    # def get_description(self, obj):
    #     if obj.description:
    #         return obj.description[:20] + "..." if len(obj.description) > 20 else obj.description[:20]
