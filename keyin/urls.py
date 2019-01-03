"""keyin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from quant_model import views as quant_model_views
from text_model import views as text_model_views
from model_summary import views as model_summary_views

router = DefaultRouter()
router.register(r'quant_model', quant_model_views.QuantModelViewSet)
router.register(r'text_model', text_model_views.TextModelViewSet)
router.register(r'model_summary', model_summary_views.ModelSummaryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1.0/', include(router.urls))
    
]
