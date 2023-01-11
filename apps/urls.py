from django.urls import path

from apps.views import qrCode
from . import views

urlpatterns = [
    path('qr/<str:data>/', views.generate_qr, name='generate_qr'),
]
