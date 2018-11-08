# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import User

# Create your models here.


class Voter(models.Model):
    user = models.OneToOneField(User)
    place_work = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name+", "+self.user.first_name+" "+self.user.username+" "+self.user.email)


class Post(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Candidate(models.Model):
    name = models.CharField(max_length=256)
    post = models.ForeignKey(Post)
    img = models.ImageField()

    def __str__(self):
        return str(self.name+" "+str(self.post))


class VotingStatus(models.Model):
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status)


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate)
    voter = models.ForeignKey(Voter)
    post = models.ForeignKey(Post)

    def __str__(self):
        return str(str(self.candidate)+" "+str(self.voter)+" "+str(self.post))


class Result(models.Model):
    candidate = models.OneToOneField(Candidate)
    votes = models.CharField(max_length=256)

    def __str__(self):
        return str(str(self.candidate)+" "+self.votes)
