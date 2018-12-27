# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from accounts.serializers import StudentSerializer
from level.models import Level
from major.models import Major
from transfer.models import IntraUni
from transfer.serializers import IntraUniSerializer, IntraUniCreateSerializer


class IntraUniAPIView(ListAPIView):
    serializer_class = IntraUniSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = IntraUni.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class IntraUniCreateAPIView(CreateAPIView):
    serializer_class = IntraUniCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = IntraUni.objects.all()
        return queryset


class IntraUniDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IntraUniSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = IntraUni.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_student(request):
    req = request.data
    student = Student.objects.get(pk=req['student'])
    major = Major.objects.get(pk=req['major'])
    level = Level.objects.get(pk=req['level'])

    student.major = major
    student.level = level
    student.save()

    return Response(StudentSerializer(student).data)
