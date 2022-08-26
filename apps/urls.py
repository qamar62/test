from django.urls import path

from apps.views import qrCode
from . import views

urlpatterns = [
    path('', views.qrCode, name='qrcode-generator'),
]
