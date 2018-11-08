# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import User

# Create your models here.


class Publication(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    description = models.TextField()
    file = models.FileField(null=True, blank=True)
