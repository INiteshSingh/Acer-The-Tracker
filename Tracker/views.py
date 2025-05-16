from django.http import HttpResponse
from django.shortcuts import render, redirect

# Home page
def home(request):
    return render(request, "Tracker/home.html")

# Tracker options page
def tracker_options(request):
    return render(request, "Tracker/tracker_options.html")

# Individual tracker page
def for_individual(request):
    return render(request, "Tracker/for_individual.html")

# Business tracker page
def for_business(request):
    return render(request, "Tracker/for_business.html")

# About us page
def about_us(request):
    return render(request, "Tracker/about_us.html")


def submit_user_data(request):
    if request.method == 'POST':
        print("POST data: ", request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        income = request.POST.get('income')  # Use get() to avoid MultiValueDictKeyError

        if not income:
            return HttpResponse("Income not provided")

        # Save to session or database
        request.session['name'] = name
        request.session['email'] = email
        request.session['income'] = income

        return redirect('dashboard')
    else:
        return HttpResponse("Invalid request method")

def dashboard(request):
    name = request.session.get('name')
    email = request.session.get('email')
    income = request.session.get('income')

    context = {
        'name': name,
        'email': email,
        'income': income
    }

    return render(request, 'Tracker/dashboard.html', context)