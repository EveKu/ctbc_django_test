from django.db import models

# Create your models here.
class QuantModel(models.Model):
    date = models.DateField()
    target_symbol = models.CharField(max_length=10, null=True, blank=True)
    target_date = models.DateField()
    use_data_start = models.DateField()
    use_data_end = models.DateField()
    result_sign = models.CharField(max_length=1, null=True, blank=True)
    result_percentage = models.CharField(max_length=10, null=True, blank=True)
    result_diff = models.CharField(max_length=10, null=True, blank=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "quant_model_table"


class Symbol(models.Model):
    symbol = models.ForeignKey(QuantModel, related_name = 'quote', on_delete=models.CASCADE)
    symbol_date = models.DateField()
    symbol_name = models.CharField(max_length=10, null=True, blank=True)
    symbol_value = models.CharField(max_length=10, null=True, blank=True)
    

    class Meta:
        db_table = "quant_model_symbol_table"


class SymbolWeight(models.Model):
    attention_weight = models.ForeignKey(QuantModel, related_name = 'top_ten_symbol', on_delete=models.CASCADE)
    symbol_name = models.CharField(max_length=10, null=True, blank=True)
    symbol_weight = models.CharField(max_length=10, null=True, blank=True)
    

    class Meta:
        db_table = "quant_model_symbol_weight_table"

class Trend(models.Model):
    trend = models.ForeignKey(QuantModel, related_name = 'trend_prediction', on_delete=models.CASCADE)
    history_date = models.DateField(null=True, blank=True)
    predict_value = models.CharField(max_length=10, null=True, blank=True)
   

    class Meta:
        db_table = "quant_model_trend_table"