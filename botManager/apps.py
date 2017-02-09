from django.apps import AppConfig


class BotmanagerConfig(AppConfig):
    name = 'botManager'
    verbose_name = 'Bot Manager'

    HOOK_TELEGRAM = 'https://requestb.in/1b0f8qb1'
