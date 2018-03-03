from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from voting.models import Post, Voter, Candidate, Vote, Result, VotingStatus


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
        )
        return queryset


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'post',
        )
        return queryset


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'candidate',
            'post',
            'voter',
        )
        return queryset


class VoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Vote.objects.all(),
                fields=('voter', 'post', 'candidate')
            )
        ]
        model = Vote
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'candidate',
            'candidate__post',
        )
        return queryset


class ResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class VotingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingStatus
        fields = '__all__'
