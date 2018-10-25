from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from transcript.serializers import ApplicationSerializer, ApplicationCreateSerializer
from transcript.models import Application

# Create your views here.


class ApplicationAPIView(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Application.objects.filter(dept=self.request.GET['dept'])
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
