# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Lecturer
from major.models import Major
from level.models import Level

# Create your models here.


class LevelAdviser(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    major = models.ForeignKey(Major)
    level = models.ManyToManyField(Level)
