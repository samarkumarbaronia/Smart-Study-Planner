from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('complete/<int:id>/', views.complete_task),
]