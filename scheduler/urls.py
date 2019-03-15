from django.urls import path

from scheduler import views

urlpatterns = [
    path('', views.index, name='index')
]
