from django.urls import  path
from django.contrib import  admin
from . import views

urlpatterns= [
    path('moderator/', views.moderator, name='moderator'),
    path('student/', views.student, name='student'),
    path('landlord/', views.landlord, name='landlord'),
    
]