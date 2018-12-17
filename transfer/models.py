# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from accounts.models import Student, User
from major.models import Major
from session.models import Session


class IntraUni(models.Model):
    student = models.ForeignKey(Student)
    major = models.ForeignKey(Major)
    reason = models.TextField()
    status = models.IntegerField()
    date = models.DateTimeField()
    session = models.ForeignKey(Session)
    paid = models.BooleanField(default=False)
    handled_by = models.ForeignKey(User, null=True, blank=True)
