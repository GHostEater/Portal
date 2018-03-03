# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Log(models.Model):
    action = models.TextField()
    user = models.TextField()
    role = models.TextField()
    date = models.DateTimeField()
    location = models.TextField()
