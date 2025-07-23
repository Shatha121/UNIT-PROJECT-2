from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Incident, Comment
from .forms import IncidentForm
from django.db.models import Count
from django.db.models import Q

# Create your views here.



def incidents_details_view(request:HttpRequest, incidents_id:int):
    incident = Incident.objects.get(pk = incidents_id)
    comments = Comment.objects.filter(incident=incident)
    return render(request, 'incidents/detail.html', {"incident":incident, "comments":comments})

def report_incident_view(request:HttpRequest):
    if request.method == "POST":
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reporter_name = request.POST.get("reporter_name")
            incident.save()
            return redirect('main:home_view')
    
    else:
        form = IncidentForm()
    
    return render(request, 'incidents/report.html', {"form":form, "CATEGORY_CHOICES":Incident._meta.get_field('category').choices})


def all_reports_view(request:HttpRequest):
    incidents = Incident.objects.all().order_by("-date_reported")
    search_result = request.GET.get("search","")
    category_filter = request.GET.get("category","")
    status_filter = request.GET.get("status","")
    if len(search_result) >= 3:
        incidents = incidents.filter(Q(title__icontains=search_result) | Q(category__icontains=search_result))
    if category_filter:
            incidents = incidents.filter(category=category_filter)
    if status_filter:
            incidents = incidents.filter(status=status_filter)
    return render(request, 'incidents/all_reports.html', {"incidents":incidents} )


def update_view(request:HttpRequest, incidents_id):
    incident = Incident.objects.get(pk=incidents_id)
    if request.method == "POST":
        incident.reporter_name = request.POST["reporter_name"]
        incident.title = request.POST["title"]
        incident.description = request.POST["description"]
        incident.category = request.POST["category"]
        if "image" in request.FILES: incident.image = request.FILES["image"]
        incident.location = request.POST["location"]
        incident.save()

        return redirect("incidents:incidents_details_view", incidents_id=incident.id)
    return render(request, "incidents/update.html", {"incident":incident})


def delete_view(request:HttpRequest, incidents_id):
    incident = Incident.objects.get(pk=incidents_id)
    incident.delete()
    return redirect("main:home_view")


def comment_views(request:HttpRequest, incidents_id:int):
    if request.method == "POST":
        incident = Incident.objects.get(pk=incidents_id)
        comment = Comment(incident=incident,author=request.POST["author"],content=request.POST["content"])
        comment.save()
    return redirect("incidents:incidents_details_view", incidents_id=incidents_id)
