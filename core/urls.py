from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download-child/', views.download_child, name='download_child'),
]
