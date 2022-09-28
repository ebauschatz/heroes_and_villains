from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.super_by_id),
    path('', views.supers_list),
    path('super/<int:super_pk>/power/<int:power_pk>/', views.add_power_to_super)
]