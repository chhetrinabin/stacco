from django.urls import path
from django.contrib import  admin
from . import views


urlpatterns = [
    path('', views.ads_list, name='ads_list'),
    path('create/', views.ads_create, name='ads_create'),
    path('view/<int:pk>/', views.ads_view, name='ads_view'),
    path('edit/<int:pk>/', views.ads_edit, name='ads_edit'),
    path('delete/<int:pk>/', views.ads_delete, name='post_delete'),
]