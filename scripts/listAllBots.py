#!/usr/bin/env python

__author__ = "stefan"

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activismBot.settings")

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

import django
django.setup()

from botManager.models import Bot

bots = Bot.objects.all()

for bot in bots:
    print(bot)
