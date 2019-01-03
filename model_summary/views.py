from model_summary.models import ModelSummary
from model_summary.serializers import ModelSummarySerializer
from rest_framework import viewsets


# Create your views here.
class ModelSummaryViewSet(viewsets.ModelViewSet):
    queryset = ModelSummary.objects.all()
    serializer_class = ModelSummarySerializer