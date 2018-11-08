# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from voting.models import Post, Voter, Result, Vote, VotingStatus, Candidate

# Register your models here.

admin.site.register(Post)
admin.site.register(Voter)
admin.site.register(Result)
admin.site.register(Vote)
admin.site.register(VotingStatus)
admin.site.register(Candidate)
