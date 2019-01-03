from rest_framework import serializers
from text_model.models import TextModel
from text_model.models import SummaryHist
from text_model.models import NewsDetail


class SummaryHistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryHist
        fields = ('history_date', 'history_result', 'history_count')

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail
        fields = ('date', 'title', 'result')


class TextModelSerializer(serializers.ModelSerializer):
    summary = SummaryHistSerializer(many=True, read_only=True)
    news = NewsDetailSerializer(many=True, read_only=True)
    class Meta:
        model = TextModel
        # fields = '__all__'
        fields = ('id', 'date', 'target_symbol', 'target_date', 'use_data_start', 'use_data_end', 'result', 'summary', 'news')
