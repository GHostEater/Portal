# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Session(models.Model):
    session = models.CharField(max_length=20, default='')
    is_current = models.BooleanField(default='1')
    actions = models.BooleanField(default='0')

    def __str__(self):
        return str(self.session)


def change_session(sender, **kwargs):
    if kwargs['instance'].is_current == 1:
        sessions = Session.objects.all()

        for session in sessions:
            session.is_current = 0
            session.save()

        sess = Session.objects.get(pk=kwargs['instance'].id)
        sess.is_current = 1
        sess.save()

# post_save.connect(change_session, sender=Session)
