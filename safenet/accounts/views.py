from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.models import Contact
from incidents.models import Incident
from main.forms import ContactForm
from django.db.models import Count
from django.db.models import Q

# Create your views here.

def sign_up(request:HttpResponse):
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"], email=request.POST["email"])
            new_user.save()
            messages.success(request,"Registered User Successfully", "alert-success")
            return redirect("accounts:sign_in")
        
        except Exception as e:
            print(e)
            messages.error(request,"Please try again. You credentials are wrong", "alert-danger")
    return render(request, "accounts/sign_up.html", {})

def sign_in(request:HttpResponse):
    if request.method == "POST":
        identifier = request.POST.get("identifier")
        password = request.POST.get("password")
        user = authenticate(request, username=identifier, password=password)

        if user == None:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("accounts:admin_dashboard")
            else:
                return redirect(request.GET.get("next","/"))
        else:
            messages.error(request,"There is no user with these information", "alert-danger")

    return render(request, "accounts/sign_in.html", {})

def log_out(request:HttpRequest):
    logout(request)
    return redirect("main:home_view")

def admin_dashboard(request:HttpRequest):
    incidents = Incident.objects.all().order_by("-date_reported")
    search_result = request.GET.get("search")
    category_filter = request.GET.get("category")
    status_filter = request.GET.get("status")
    rank_filter = request.GET.get("reporter_rank")
    
    if search_result and len(search_result) >= 1:
        incidents = incidents.filter(Q(title__icontains=search_result) | Q(category__icontains=search_result))
    if category_filter:
            incidents = incidents.filter(category=category_filter)
    if status_filter:
            incidents = incidents.filter(status=status_filter)
    if rank_filter:
        if rank_filter == "None":
            incidents = [i for i in incidents if i.reporter_name.lower().strip() =="anonymous" or i.reporter_rank() is None] 
        else: 
            incidents =[ i for i in incidents if i.reporter_name.lower().strip() !="anonymous" and i.reporter_rank() == rank_filter]
    total_incidents = Incident.objects.count()
    open_incidents = Incident.objects.filter(status="open").count()
    closed_incidents = Incident.objects.filter(status="closed").count()
    Category_Dict = dict(Incident.CATEGORY_CHOICES)
    top_value_category = (
        Incident.objects.values('category').annotate(count=Count('category')).order_by('-count').values_list('category', flat=True)[:3]
    )
    top_categories = [Category_Dict[value] for value in top_value_category]
    ranks = ["Gold", "Silver", "Bronze"]
    category_choices = Incident._meta.get_field('category').choices
    status_choices = Incident._meta.get_field('status').choices

    return render(request, 'accounts/admin_dashboard.html', {'total_incidents':total_incidents,'open_incidents':open_incidents,'closed_incidents':closed_incidents,'top_categories':top_categories,'recent_incidents':incidents, 'ranks':ranks, 'category_choices':category_choices, 'status_choices':status_choices})


def change_status_view(request:HttpRequest, report_id):
    incident = Incident.objects.get(pk = report_id)
    new_status = request.POST.get("status")
    if new_status in ["open", "closed"]:
        incident.status = new_status
        incident.save()
    return redirect("accounts:admin_dashboard")