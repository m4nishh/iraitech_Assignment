
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('v1/', views.input, name="input"),
    path('calc', views.calc, name="calc")

]
