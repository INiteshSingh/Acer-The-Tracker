from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"Tracker/home.html")

def tracker_options(request):
    return render(request,"Tracker/tracker_options.html")

def for_individual(request):
    return render(request,"Tracker/for_individual.html")

def for_business(request):
    return render(request,"Tracker/for_business.html")

def about_us(request):
    return render(request,"Tracker/about_us.html")