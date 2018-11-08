# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from publication.serializers import PublicationSerializer, PublicationCreateSerializer
from publication.models import Publication

# Create your views here.


class PublicationAPIView(ListAPIView):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        queryset = Publication.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PublicationUserAPIView(ListAPIView):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        queryset = Publication.objects.filter(user=self.request.GET['user'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PublicationCreateAPIView(CreateAPIView):
    serializer_class = PublicationCreateSerializer

    def get_queryset(self):
        queryset = Publication.objects.all()
        return queryset


class PublicationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationSerializer

    def get_queryset(self):
        queryset = Publication.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
