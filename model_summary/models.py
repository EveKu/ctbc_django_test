from django.db import models

# Create your models here.
class ModelSummary(models.Model):
    update = models.DateField()
    model_type = models.CharField(max_length=2, null=True, blank=True)
    target_symbol = models.CharField(max_length=10, null=True, blank=True)
    loss = models.CharField(max_length=10, null=True, blank=True)
    accuracy = models.CharField(max_length=10, null=True, blank=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "model_summary_table"