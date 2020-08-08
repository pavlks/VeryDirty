from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:threshold_date>/<int:page>/', views.index, name='index'),
]