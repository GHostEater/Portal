# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Lecturer
from major.models import Major
from level.models import Level

# Create your models here.


class LevelAdviser(models.Model):
    lecturer = models.OneToOneField(Lecturer)
    major = models.ForeignKey(Major)
    level = models.ManyToManyField(Level)

    def __str__(self):
        return str(str(self.lecturer)+" "+str(self.major)+" "+str(self.level))
