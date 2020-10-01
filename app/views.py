from django.shortcuts import render, get_object_or_404, redirect
from .models import Thinkcentre, Thinkstation, Thinkpad, Esports, Campuscomputing, Securityandservices, Datacentered
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    return render(request, '404.html')

def thinkCenter(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataThinkcentre(request):
    p = Thinkcentre(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/thinkcenter")

def thinkstation(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataThinkstation(request):
    p = Thinkstation(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/thinkstation")


def thinkpad(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataThinkpad(request):
    p = Thinkpad(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/thinkpad")


def esports(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataEsports(request):
    p = Esports(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/esports")


def campuscomputing(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataCampuscomputing(request):
    p = Campuscomputing(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/campuscomputing")



def securityandservices(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataSecurityandservices(request):
    p = Securityandservices(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/securityandservices")



def datacentered(request):
    return render(request, 'index.html')

@csrf_exempt
def postDataDatacentered(request):
    p = Datacentered(
    First_Name=request.POST.get('fname'), 
    Last_Name=request.POST.get('lname'), 
    Institution = request.POST.get('institution'), 
    Title = request.POST.get('title'),
    Email=request.POST.get('email'),
    Country = request.POST.get('country')
    )
    p.save()
    return redirect("/datacentered")