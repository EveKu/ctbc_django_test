from django.contrib import admin
from .models import ModelSummary
from . import forms
# Register your models here.

class ModelSummaryAdmin(admin.ModelAdmin):
    form = forms.ModelSummaryDefaultForm


admin.site.register(ModelSummary)
