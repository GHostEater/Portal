# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import Student, StudentAffairs
from room.models import Room
from session.models import Session

# Create your models here.


class RoomAllocation(models.Model):
    student = models.ForeignKey(Student)
    room = models.ForeignKey(Room)
    session = models.ForeignKey(Session)
    allocated_by = models.ForeignKey(StudentAffairs)

    def __str__(self):
        return str(str(self.student)+" "+str(self.room)+" "+str(self.session)+" "+str(self.allocated_by))
