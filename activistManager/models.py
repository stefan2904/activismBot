from django.db import models

from botManager.models import Bot


class Activist(models.Model):
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    reg_date = models.DateTimeField('Date registered', auto_now_add=True)
    bot = models.ForeignKey(Bot)  # on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({}: {})'.format(self.name, self.bot.name, self.identifier)
