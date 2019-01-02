from django.db import models

# Create your models here.
class QuantModel(models.Model):
    date = models.DateField()
    target_symbol = models.TextField(null=True, blank=True)
    target_date = models.DateField()
    use_data_start = models.DateField()
    use_data_end = models.DateField()
    result_sign = models.TextField(null=True, blank=True)
    result_percentage = models.TextField(null=True, blank=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "quant_model_table"