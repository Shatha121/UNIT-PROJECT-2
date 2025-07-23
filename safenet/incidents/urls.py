from django.urls import path 
from . import views

app_name = "incidents"

urlpatterns = [
    path('report/', views.report_incident_view, name="report_incident_view"),
    path('all_reports/', views.all_reports_view, name='all_reports_view'),
    path('<int:incidents_id>/detail/', views.incidents_details_view, name="incidents_details_view"),
    path('<int:incidents_id>/update/',views.update_view, name='update_view'),
    path('<int:incidents_id>/delete/',views.delete_view, name="delete_view"),
    path('comment/add/<plant_id>/', views.comment_views, name="comment_views"),
]