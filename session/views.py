# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from session.serializers import SessionSerializer
from session.models import Session
from accounts.models import Student
from levelAdviser.models import LevelAdviser
from level.models import Level

# Create your views here.


class SessionAPIView(ListAPIView):
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Session.objects.all()


class SessionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Session.objects.all()


class SessionCurrentAPIView(RetrieveAPIView):
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Session.objects.all()
    lookup_field = 'is_current'


@csrf_exempt
def session_actions(request):
    students = Student.objects.all()
    advisers = LevelAdviser.objects.all()
    session = Session.objects.get(is_current=True)

    for student in students:
        if student.level.level <= '300':
            level = int(Level.objects.get(pk=student.level.id).id) + 1
            level = Level.objects.get(pk=level)
            student.level = level
            student.save()
    # for adviser in advisers:
    #     lvl = adviser.level.all()
    #     for lvl in lvl:
    #         lvli = int(lvl.id) + 1
    #         adviser.level.remove(lvl)
    #         adviser.level.add(lvli)
    #     adviser.save()
    session.actions = True
    session.save()
    return JsonResponse({}, safe=False, status=200)
