from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.super_by_id),
    path('', views.supers_list),
]