from django.apps import AppConfig


class BotmanagerConfig(AppConfig):
    name = 'botManager'
    verbose_name = 'Bot Manager'

    HOOK_TELEGRAM = 'https://cloud.failing.systems/activistBot/'
