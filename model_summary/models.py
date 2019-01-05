from django.db import models

# Create your models here.
class ModelSummary(models.Model):
    update = models.DateField()
    model_type = models.CharField(max_length=2, null=True, blank=True)
    target_symbol = models.CharField(max_length=10, null=True, blank=True)
    loss = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    model_path = models.CharField(max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=255, editable=False, unique=True, null=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "model_summary_table"