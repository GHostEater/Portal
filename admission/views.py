from __future__ import unicode_literals

from django.template.loader import get_template
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from admission.serializers import (PinSerializer,
                                   PinCreateSerializer,
                                   ApplicationSerializer,
                                   ApplicationCreateSerializer,)
from admission.models import Pin, Application

# Create your views here.


class PinAPIView(ListAPIView):
    serializer_class = PinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Pin.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PinCreateAPIView(CreateAPIView):
    serializer_class = PinCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Pin.objects.all()
        return queryset


class PinDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PinSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pin'

    def get_queryset(self):
        queryset = Pin.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ApplicationAPIView(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Application.objects.filter(programme=self.request.GET['programme'],
                                              admitted=self.request.GET['admitted'],
                                              session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ApplicationSingleDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    lookup_field = 'email'

    def get_queryset(self):
        queryset = Application.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ApplicationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ApplicationCreateAPIView(CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    queryset = Application.objects.all()


@api_view(['GET'])
def email(request):
    app = Application.objects.get(pk=request.GET['id'])
    app.url = request.GET['dean_url']
    template = get_template('email_dean.html')
    context = {'app': app}
    content = template.render(context)
    subject = "Fountain University - Your Student Applied For Admission"

    message = MailerMessage()
    message.subject = subject
    message.to_address = app.email_dean
    message.bcc_address = 'transfers@fuo.edu.ng'
    message.from_address = 'transfers@fuo.edu.ng'
    message.content = ""
    message.html_content = content
    message.app = "Fountain University Mailing System"
    message.save()

    app.url = request.GET['hod_url']
    template = get_template('email_hod.html')
    context = {'app': app}
    content = template.render(context)
    subject = "Fountain University - Your Student Applied For Admission"

    message = MailerMessage()
    message.subject = subject
    message.to_address = app.email_hod
    message.bcc_address = 'transfers@fuo.edu.ng'
    message.from_address = 'transfers@fuo.edu.ng'
    message.content = ""
    message.html_content = content
    message.app = "Fountain University Mailing System"
    message.save()
    return Response('ok')
