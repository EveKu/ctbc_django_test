from rest_framework import serializers
from quant_model.models import QuantModel
from quant_model.models import Symbol
from quant_model.models import SymbolWeight
from quant_model.models import Trend

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('symbol_name', 'symbol_date', 'symbol_value')

class SymbolWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymbolWeight
        fields = ('symbol_name', 'symbol_weight')

class TrendWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ('history_date', 'predict_value')

class QuantModelSerializer(serializers.ModelSerializer):
    quote = SymbolSerializer(many=True, read_only=True)
    top_ten_symbol = SymbolWeightSerializer(many=True, read_only=True)
    trend_prediction = TrendWeightSerializer(many=True, read_only=True)
    class Meta:
        model = QuantModel
        # fields = '__all__'
        fields = ('id', 'date', 'target_symbol', 'target_date', 'use_data_start', 'use_data_end', 'result_sign', 'result_percentage', 'result_diff','trend_prediction', 'top_ten_symbol', 'quote')

     