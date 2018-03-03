from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from paymenttomajor.models import PaymentToMajor


class PaymentToMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentToMajor
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'payment_type',
            'major',
            'major__dept',
            'major__dept__college',
            'level',
        )
        return queryset


class PaymentToMajorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=PaymentToMajor.objects.all(),
                fields=('payment_type', 'major', 'level')
            )
        ]
        model = PaymentToMajor
        fields = '__all__'
