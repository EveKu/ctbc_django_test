from rest_framework import serializers
from model_summary.models import ModelSummary

class ModelSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSummary
        # fields = '__all__'
        fields = ('id', 'target_symbol', 'model_type', 'update', 'loss', 'accuracy')
