from django.urls import path 
from . import views

app_name = "incidents"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('report/', views.report_incident_view, name="report_incident_view"),
    path('<report_id>/detail', views.incidents_details_view, name="incidents_details_view"),
]