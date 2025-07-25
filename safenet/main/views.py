from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Contact
from incidents.models import Incident
from .forms import ContactForm
from django.db.models import Count
from django.db.models import Q

# Create your views here.

def home_view(request:HttpRequest):
    total_incidents = Incident.objects.count()
    open_incidents = Incident.objects.filter(status="open").count()
    closed_incidents = Incident.objects.filter(status="closed").count()
    Category_Dict = dict(Incident.CATEGORY_CHOICES)


    top_value_category = (
        Incident.objects.values('category').annotate(count=Count('category')).order_by('-count').values_list('category', flat=True)[:3]
    )
    top_categories = [Category_Dict[value] for value in top_value_category]

    recent_incidents = Incident.objects.all().order_by('-date_reported')[:4]
    return render(request, 'main/home.html', {'total_incidents':total_incidents,'open_incidents':open_incidents,'closed_incidents':closed_incidents,'top_categories':top_categories,'recent_incidents':recent_incidents})


def contact_us_view(request:HttpRequest):
    contect_form = ContactForm()
    sumbitted = False
    if request.method == "POST":
        contect_form = ContactForm(request.POST, request.FILES)
        if contect_form.is_valid():
            contect_form.save()
            sumbitted = True
        else:
            print('not valid form')
    return render(request, 'main/contact_us.html',{"contect_form":contect_form, "sumbitted":sumbitted})


def dark_mode_view(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)
    response.set_cookie("mode", "dark", max_age=60*60*24*7)
    return response

def light_mode_view(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)
    response.delete_cookie("mode")
    return response