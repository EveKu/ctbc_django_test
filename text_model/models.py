from django.db import models

# Create your models here.
class TextModel(models.Model):
    date = models.DateField()
    target_symbol = models.CharField(max_length=10, null=True, blank=True)
    target_date = models.DateField()
    use_data_start = models.DateField()
    use_data_end = models.DateField()
    #result_sign = models.CharField(max_length=1, null=True, blank=True)
    result = models.CharField(max_length=10, null=True, blank=True)
    checksum = models.CharField(max_length=255, unique=True, null=True, blank=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "text_model_table"


class SummaryHist(models.Model):
    summary_hist = models.ForeignKey(TextModel, related_name = 'summary', on_delete=models.CASCADE)
    history_date = models.DateField(null=True, blank=True)
    history_result = models.CharField(max_length=2, null=True, blank=True)
    history_count = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "text_model_summary_hist_table"


class NewsDetail(models.Model):
    news_detail = models.ForeignKey(TextModel, related_name = 'news', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        db_table = "text_model_news_detail_table"       