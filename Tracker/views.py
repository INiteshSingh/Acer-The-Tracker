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

# Form to add expenses after income is submitted
def expenses_form(request):
    income = request.session.get('income')
    if not income:
        return HttpResponse("Income data not found. Please go back and enter your income.")

    return render(request, "Tracker/expenses_form.html", {'income': income})

# Process the submitted income and redirect to the expenses form
def submit_income(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        income = request.POST.get('income')

        # Store data in session (or save to DB if preferred)
        request.session['name'] = name
        request.session['email'] = email
        request.session['income'] = income

        # Redirect to the form to add expenses
        return redirect('expenses_form')

    return HttpResponse("Invalid Method")

def submit_expense(request):
    if request.method == 'POST':
        names = request.POST.getlist('expense_name[]')
        amounts = request.POST.getlist('expense_amount[]')

        expenses = list(zip(names, amounts))
        income = request.session.get('income', 0)

        return render(request, 'Tracker/summary.html', {
            'income': income,
            'expenses': expenses
        })
    return HttpResponse("Invalid Method")
