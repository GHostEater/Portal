# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Semester(models.Model):
    semester = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.semester)
