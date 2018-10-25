# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from college.models import College
# Create your models here.


class Dept(models.Model):
    name = models.CharField(max_length=255, default='')
    college = models.ForeignKey(College)

    def __str__(self):
        return str(self.name)
