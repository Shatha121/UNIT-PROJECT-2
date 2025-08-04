from django.urls import path 
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
]



