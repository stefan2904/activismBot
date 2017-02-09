from django.db import models

from botManager.apps import BotmanagerConfig as config


class Bot(models.Model):
    name = models.CharField(max_length=200, editable=False)
    endpoint = models.CharField(max_length=200)

    def __str__(self):
        typ = getBotType(self)
        return '{:>2}:  {} ({})'.format(self.id, self.name, typ)

    def send(self, msg):
        pass


class TelegramBot(Bot):
    authkey = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        from twx.botapi import TelegramBot as TwxTelegramBot
        bot = TwxTelegramBot(self.authkey)
        try:
            bot.set_webhook(url=config.HOOK_TELEGRAM)
            bot.update_bot_info().wait()
            self.name = bot.username
        except Exception:
            self.name = self.authkey
        super(TelegramBot, self).save(*args, **kwargs)  # Call the "real" save()


class FacebookBot(Bot):
    def __init__(self):
        raise NotImplementedError('Facebook Bots not yet implemented, sorry ...')


def getBotType(bot):
    # see https://docs.djangoproject.com/en/1.10/topics/db/models/#multi-table-inheritance
    try:
        _ = bot.facebookbot
        return 'Facebook'
    except Exception:
        pass
    try:
        _ = bot.telegrambot
        return 'Telegram'
    except Exception:
        pass
    return '?'
