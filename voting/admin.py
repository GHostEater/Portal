# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from voting.models import Post, Voter, Result, Vote, VotingStatus, Candidate

# Register your models here.

admin_site.register(Post)
admin_site.register(Voter)
admin_site.register(Result)
admin_site.register(Vote)
admin_site.register(VotingStatus)
admin_site.register(Candidate)
