from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('contact_us/', views.contact_us_view, name='contact_us_view'),
]


