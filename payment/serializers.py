from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'payment_type',
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'application',
            'application__session',
            'application__level',
            'application__choice',
            'application__choice__dept',
            'application__choice__dept__college',
            'session',
        )
        return queryset


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
