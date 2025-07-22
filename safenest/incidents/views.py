from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Incident
from .forms import IncidentForm
from comments.forms import CommentForm

# Create your views here.



def home_view(request:HttpRequest):
    incidents = Incident.objects.all().order_by('-date_reported')
    return render(request, 'incidents/home.html', {"incidents":incidents})

def incidents_details_view(request:HttpRequest, incidents_id:int):
    incident = Incident.objects.get(pk = incidents_id)
    return render(request, 'incidents/detail.html', {"incident":incident})

def report_incident_view(request:HttpRequest):
    if request.method == "POST":
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reporter = request.user
            incident.save()
            return redirect('incident_detail', pk=incident.pk)
    
    else:
        form = IncidentForm()
    
    return render(request, 'incidents/report.html', {"form":form})

def incident_list_view(request:HttpRequest):
    category = request.GET.get('category')
    status = request.GET.get('status')
    location = request.GET.get('location')

    incidents = Incident.objects.all()

    if category:
        incidents = incidents.filter(category=category)
    if status:
        incidents = incidents.filter(status=status)
    if location:
        incidents = incidents.filter(location=location)

    context = {
        'incidents': incidents,
        'categories': Incident.CATEGORY_CHOICES,
        'statuses': Incident.STATUS_CHOICES,
    }

    return render(request, 'incidents/home.html', context)