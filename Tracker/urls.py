from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("tracker_options",views.tracker_options,name="tracker_options"),
    path("for_individual",views.for_individual,name="for_individual"),
    path("for_business",views.for_business,name="for_business"),
    path("about_us",views.about_us,name="about_us"),
    path("submit_income",views.submit_expense,name="submit_income"),
    path("submit_expenses", views.submit_expense, name="submit_expense"),
    path("submit/", views.submit_income, name="submit_income"),
]
