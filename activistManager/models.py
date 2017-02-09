from django.db import models


class Activist(models.Model):
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    reg_date = models.DateTimeField('Date registered')
