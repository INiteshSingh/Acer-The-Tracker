from django.http import HttpResponse
from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import io, base64
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


def submit_income(request):
    if request.method == 'POST':
        income = request.POST.get('income')  # Use get() to avoid MultiValueDictKeyError
        request.session['income'] = income
        return redirect('add_expenses')
    return render('add_expenses')


def add_expenses(request):
    if request.method == "POST":
        name = request.POST.get('expense_name')
        amount = request.POST.get('expense_amount')

        expenses = request.session.get('expenses',[])
        expenses.append({"name" : name, "amount" : float(amount)})
        request.session['expenses'] = expenses

    expenses = request.session.get('expenses',[])
    income = float(request.session.get('income',0))

    chart = None
    if expenses:
        lables = [e['name'] for e in expenses]
        values = [e['amount'] for e in expenses]

        fig, ax = plt.subplots()
        ax.pie(values, labels = lables, autopct = '%1.1f%%')
        ax.set_title("Expense Distribution")
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        chart = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'add_expenses.html', {
        'income': income,
        'expenses': expenses,
        'chart': chart
    })
    

def view_chart(request):
    expenses = request.session.get('expenses',[])
    income = float(request.session.get('income',0))

    labels = [e['name'] for e in expenses]
    values = [e['amount'] for e in expenses]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Expense Distribution")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()
    chart = base64.b64encode(image_png).decode('utf-8')
    return render(request, 'chart.html', {'chart' : chart, 'income' : income, 'expenses' : expenses})