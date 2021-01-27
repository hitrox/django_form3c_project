from django.urls import path
from . import views

urlpatterns = [
    path('', views.start,name='form-start'),
    path('home/',views.home,name='form-home'),
]