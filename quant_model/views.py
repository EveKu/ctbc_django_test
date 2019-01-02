from quant_model.models import QuantModel
from quant_model.serializers import QuantModelSerializer
from rest_framework import viewsets


# Create your views here.
class QuantModelViewSet(viewsets.ModelViewSet):
    queryset = QuantModel.objects.all()
    serializer_class = QuantModelSerializer