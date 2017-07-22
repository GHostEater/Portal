# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from course.models import Course
from major.models import Major
from level.models import Level

# Create your models here.


class CourseToMajor(models.Model):
    course = models.ForeignKey(Course)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)

    def __str__(self):
        return str(self.course) + ', ' + str(self.major) + ', ' + str(self.level)
