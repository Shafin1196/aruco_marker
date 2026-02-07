from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('test/',views.generate_aruco, name='hello_api'),
]
