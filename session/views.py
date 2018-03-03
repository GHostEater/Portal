# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from session.serializers import SessionSerializer
from session.models import Session
from accounts.models import Student
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
    queryset = Session.objects.all()
    lookup_field = 'is_current'


class SessionAdmissionAPIView(RetrieveAPIView):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()
    lookup_field = 'is_admission'


@csrf_exempt
def session_actions(request):
    students = Student.objects.all()
    session = Session.objects.get(is_current=True, actions=False)

    if session:
        for student in students:
            if student.level.level <= '300':
                level = int(Level.objects.get(pk=student.level.id).id) + 1
                level = Level.objects.get(pk=level)
                student.level = level
                student.save()
        session.actions = True
        session.save()
    return JsonResponse({}, safe=False, status=200)
