# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from course.models import Course

# Create your models here.


class Courseware(models.Model):
    course = models.ForeignKey(Course)
    file = models.FileField(null=True, blank=True)
    info = models.TextField()
    
    def __str__(self):
        return str(self.course) + ", " + str(self.info)
