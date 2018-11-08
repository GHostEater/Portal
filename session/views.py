# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    return Response({})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_session(request):
    body = request.data

    sessions = Session.objects.all()

    if body['is_current']:
        for session in sessions:
            session.is_current = False
            session.save()
    if body['is_admission']:
        for session in sessions:
            session.is_admission = False
            session.save()

    session = Session()
    session.session = body['session']
    session.is_current = body['is_current']
    session.is_admission = body['is_admission']
    session.save()

    serial = SessionSerializer(session).data

    return Response(serial)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_current(request):
    body = request.data

    sessions = Session.objects.all()
    session = Session.objects.get(pk=body['id'])

    for sess in sessions:
        sess.is_current = False
        sess.save()

    session.is_current = True
    session.save()

    serial = SessionSerializer(session).data

    return Response(serial)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_admission(request):
    body = request.data

    sessions = Session.objects.all()
    session = Session.objects.get(pk=body['id'])

    for sess in sessions:
        sess.is_admission = False
        sess.save()

    session.is_admission = True
    session.save()

    serial = SessionSerializer(session).data

    return Response(serial)
