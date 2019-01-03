from text_model.models import TextModel
from text_model.serializers import TextModelSerializer
from rest_framework import viewsets


# Create your views here.
class TextModelViewSet(viewsets.ModelViewSet):
    queryset = TextModel.objects.all()
    serializer_class = TextModelSerializer