# -*- coding: utf-8 -*-
import datetime
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Lecturer, Dean
from courseresulteditrequest.serializers import LogSerializer, RequestSerializer, LogCreateSerializer, RequestCreateSerializer
from courseresulteditrequest.models import Log, Request

# Create your views here.


class RequestAPIView(ListAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Request.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class RequestCreateAPIView(CreateAPIView):
    serializer_class = RequestCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Request.objects.all()
        return queryset


class RequestDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Request.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LogAPIView(ListAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LogCreateAPIView(CreateAPIView):
    serializer_class = LogCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.all()
        return queryset


class LogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Log.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notify_dean(request):
    req = request.GET
    lecturer = Lecturer.objects.get(pk=req['lecturer'])
    dean = Dean.objects.get(college=lecturer.dept.college)

    subject = req['school_name'] + " - Lecturer Applied For Edit Privileges"

    message = MailerMessage()
    message.subject = subject
    message.to_address = dean.user.username
    message.from_address = req['email']
    message.content = lecturer.user.last_name+", "+lecturer.user.first_name+' applied for edit privileges, check and ' \
                                                                            'review application '
    message.app = req['school_name'] + " Mailing System"
    message.save()
    return Response({})


@api_view(['GET'])
def auto_disable_edit(request):
    requests = Request.objects.all()
    for req in requests:
        try:
            date_compare = req.end_date <= datetime.datetime.now()
        except:
            continue
        if date_compare:
            req.delete()
    return Response({})
