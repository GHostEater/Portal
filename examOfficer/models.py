# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dept.models import Dept
from accounts.models import Lecturer

# Create your models here.


class ExamOfficer(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    dept = models.OneToOneField(Dept)
