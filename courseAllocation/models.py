# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from course.models import Course
from accounts.models import Lecturer
from session.models import Session
from dept.models import Dept

# Create your models here.


class CourseAllocation(models.Model):
    position_choices = (
        (1, 'Coordinator'),
        (2, 'Assisting'),
    )
    course = models.ForeignKey(Course)
    lecturer = models.ForeignKey(Lecturer, related_name='lecturer')
    allocatedBy = models.ForeignKey(Lecturer, related_name='allocatedBy')
    session = models.ForeignKey(Session)
    position = models.IntegerField(choices=position_choices, default=2)
    dept = models.ForeignKey(Dept)

    def __str__(self):
        return str(self.course) + ", " + str(self.lecturer) + ", " + str(self.session)
