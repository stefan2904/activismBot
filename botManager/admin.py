from django.contrib import admin

from .models import Bot, TelegramBot, FacebookBot

# admin.site.register(Bot)
admin.site.register(TelegramBot)
admin.site.register(FacebookBot)
