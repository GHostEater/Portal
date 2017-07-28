from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from paymentToMajor.models import PaymentToMajor
from paymentType.models import PaymentType
from paymentType.serializers import PaymentTypeSerializer


class PaymentToMajorSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    major = serializers.SerializerMethodField()
    majorId = serializers.SerializerMethodField()
    paymentType = serializers.SerializerMethodField()

    class Meta:
        model = PaymentToMajor
        fields = '__all__'

    def get_level(self, obj):
        return str(obj.level.level)

    def get_major(self, obj):
        return str(obj.major.name)

    def get_majorId(self, obj):
        return str(obj.major.id)

    def get_paymentType(self, obj):
        return PaymentTypeSerializer(PaymentType.objects.get(pk=obj.paymentType.id)).data


class PaymentToMajorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=PaymentToMajor.objects.all(),
                fields=('paymentType', 'major', 'level')
            )
        ]
        model = PaymentToMajor
        fields = '__all__'
