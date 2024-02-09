from django.db import models
from django.utils.translation import gettext_lazy as _


class TelegramUser(models.Model):
    full_name = models.CharField(_("Name"), max_length=255)
    username = models.CharField(_("Telegram username"), max_length=255, null=True)
    phone_number = models.CharField(_("Phone number"), max_length=20, null=True)
    chat_id = models.BigIntegerField("Telegram chat id", unique=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.chat_id}"
