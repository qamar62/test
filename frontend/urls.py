from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainSite, name="home"),
    path('contact-us', views.contact, name="contact-us"),
]
