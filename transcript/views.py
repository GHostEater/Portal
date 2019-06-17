from __future__ import unicode_literals

from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from transcript.serializers import ApplicationSerializer, ApplicationCreateSerializer
from transcript.models import Application


# Create your views here.


class ApplicationAPIView(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Application.objects.filter(dept=self.request.GET['dept'],
                                              status=self.request.GET['status'],
                                              paid=True)
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


class ApplicationStudentAPIView(ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.filter(matric_no=self.request.GET['matric_no'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@api_view(['GET'])
def notify_registrar(request):
    req = request.GET
    app = Application.objects.get(pk=req['id'])

    subject = "Fountain University - Application For Transcript"

    message = MailerMessage()
    message.subject = subject
    message.to_address = "registrar@fuo.edu.ng"
    message.from_address = "no_reply@fuo.edu.ng"
    message.content = app.last_name+", "+app.first_name+" "+app.matric_no+' applied for transcript, check and ' \
                                                                          'review application '
    message.app = "Fountain University Mailing System"
    message.save()
    return Response({})
