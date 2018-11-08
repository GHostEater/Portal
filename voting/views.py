# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from voting.serializers import (PostSerializer, CandidateSerializer, VoterSerializer, VoteSerializer,
                                VoteCreateSerializer, ResultSerializer, ResultCreateSerializer, VotingStatusSerializer)
from voting.models import Post, Voter, Result, Vote, VotingStatus, Candidate
from accounts.models import User


# Create your views here.


class PostAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()


@csrf_exempt
def voter_create(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    date_birth = body['date_birth']

    user = User()
    user.username = body['username']
    user.password = body['password']
    user.first_name = body['first_name']
    user.last_name = body['last_name']
    user.email = body['email']
    user.type = '10'
    user.sex = body['sex']
    user.date_birth = date_birth
    user.nationality = body['nationality']
    user.state_origin = body['state_origin']
    user.lga = body['lga']
    user.religion = body['religion']
    user.address = body['address']
    user.town = body['town']
    user.phone = body['phone']
    user.save()

    voter = Voter()
    voter.user = user
    voter.place_work = body['place_work']
    voter.save()

    serial = VoterSerializer(voter)

    return JsonResponse(serial.data, safe=False, status=200)


class VoterAPIView(ListAPIView):
    serializer_class = VoterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Voter.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class VoterDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VoterSerializer
    lookup_field = 'user'

    def get_queryset(self):
        queryset = Voter.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CandidateAPIView(ListAPIView):
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Candidate.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CandidateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Candidate.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class VoteAPIView(ListAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Vote.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class VoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Vote.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class VoteCreateAPIView(CreateAPIView):
    serializer_class = VoteCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Vote.objects.all()


class ResultAPIView(ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Result.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ResultDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Result.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class ResultCreateAPIView(CreateAPIView):
    serializer_class = ResultCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Result.objects.all()


class VotingStatusAPIView(RetrieveUpdateAPIView):
    serializer_class = VotingStatusSerializer
    queryset = VotingStatus.objects.all()
