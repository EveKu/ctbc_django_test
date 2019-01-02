from rest_framework import serializers
from quant_model.models import QuantModel


class QuantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantModel
        # fields = '__all__'
        fields = ('id', 'date', 'target_symbol')