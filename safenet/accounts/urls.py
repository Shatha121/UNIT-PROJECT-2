from django.urls import path 
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.log_out, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin_dashboard/change_status/<int:report_id>', views.change_status_view, name="change_status_view"),
]



