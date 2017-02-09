import json

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from twx.botapi import TelegramBot as TwxTelegramBot
from twx.botapi import Update as TwxUpdate

from botManager.apps import BotmanagerConfig as config


class Bot(models.Model):
    name = models.CharField(max_length=200, editable=False)
    endpoint = models.CharField(max_length=200)

    def __str__(self):
        typ = getBotType(self)
        return '{:>2}:  {} ({})'.format(self.id, self.name, typ)

    def process(self, request):
        "process a request to us from a bot"
        return getBot(self).process(request)

    def send(self, msg):
        "send a message from us to the bot"
        pass


class TelegramBot(Bot):
    authkey = models.CharField(max_length=200)
    lastMsg = models.IntegerField()

    def save(self, *args, **kwargs):
        bot = TwxTelegramBot(self.authkey)
        try:
            bot.set_webhook(url=config.HOOK_TELEGRAM + self.endpoint)
            bot.update_bot_info().wait()
            self.name = bot.username
        except Exception:
            self.name = self.authkey
        super(TelegramBot, self).save(*args, **kwargs)  # Call the "real" save()

    def process(self, request):
        from activistManager.models import Activist
        update = TwxUpdate.from_result([json.loads(request.body.decode('utf-8'))])[0]
        activist_id = update.message.chat.id
        try:
            activist = Activist.objects.get(identifier=activist_id)
        except ObjectDoesNotExist:
            activist = Activist(identifier=activist_id)

        activist.name = update.message.chat.first_name
        activist.username = update.message.chat.username
        activist.bot = self
        activist.save()
        return 'thanks!'
        # raise NotImplementedError('Telegram processing not yet implemented, sorry ...')


class FacebookBot(Bot):
    def __init__(self):
        raise NotImplementedError('Facebook Bots not yet implemented, sorry ...')

    def process(self, request):
        raise NotImplementedError('Facebook Bots not yet implemented, sorry ...')


def getBot(bot):
    # see https://docs.djangoproject.com/en/1.10/topics/db/models/#multi-table-inheritance
    try:
        return bot.facebookbot
    except Exception:
        pass
    try:
        return bot.telegrambot
    except Exception:
        pass
    return None


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
