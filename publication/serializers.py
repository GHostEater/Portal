from rest_framework import serializers
from publication.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
        )
        return queryset


class PublicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
