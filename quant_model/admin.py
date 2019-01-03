from django.contrib import admin
from .models import QuantModel
from .models import Symbol
from .models import SymbolWeight
from .models import Trend
# Register your models here.



admin.site.register(QuantModel)
admin.site.register(Symbol)
admin.site.register(SymbolWeight)
admin.site.register(Trend)