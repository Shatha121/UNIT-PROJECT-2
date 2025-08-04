from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
                return redirect("main:admin_dashboard")
            else:
                return redirect("main:home_view")
        else:
            messages.error(request,"There is no user with these information", "alert-danger")

    return render(request, "account/sign_in.html", {})