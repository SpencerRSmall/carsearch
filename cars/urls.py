from django.urls import path
from cars import views

urlpatterns = [
    path('cars/', views.year_selector),
   