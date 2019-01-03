from django.contrib import admin
from .models import TextModel
from .models import SummaryHist
from .models import NewsDetail
# Register your models here.



admin.site.register(TextModel)
admin.site.register(SummaryHist)
admin.site.register(NewsDetail)