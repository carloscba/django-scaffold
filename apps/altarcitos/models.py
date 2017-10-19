from __future__ import unicode_literals

from django.db import models

class Altarcitos(models.Model):
    name = models.CharField(max_length=255, unique = False)
    username = models.CharField(max_length=255, unique = False)
    message = models.TextField()
    photo = models.URLField()
    uid =  models.CharField(max_length=255)

