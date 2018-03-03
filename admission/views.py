from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
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
