# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from accounts.models import Lecturer
from course.models import Course
from session.models import Session


class Log(models.Model):
    lecturer = models.ForeignKey(Lecturer, related_name="result_upload_lecturer")
    course = models.ForeignKey(Course)
    session = models.ForeignKey(Session)
    date = models.DateTimeField()
    upload_type = models.TextField()
    uploaded = models.TextField()
