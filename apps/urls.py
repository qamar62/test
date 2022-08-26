from django.urls import path

from apps.views import qrCode
from . import views

urlpatterns = [
    path('qrcode/', views.qrCode, name='qrcode-generator'),
]
