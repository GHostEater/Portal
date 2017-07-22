# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Lecturer
from dept.models import Dept

# Create your models here.


class Hod(models.Model):
    lecturer = models.OneToOneField(Lecturer)
    dept = models.OneToOneField(Dept)

    def __str__(self):
        return str(self.lecturer.user) + ", " + str(self.dept.name)
