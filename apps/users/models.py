from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    displayName = models.CharField(max_length=255, unique = True)
    email = models.EmailField(unique = True, blank = True)
    photoURL = models.URLField()
    uid =  models.CharField(max_length=255, unique = True)

