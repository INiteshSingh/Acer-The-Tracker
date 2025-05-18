from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("tracker_options",views.tracker_options,name="tracker_options"),
    path("for_individual",views.for_individual,name="for_individual"),
    path("for_business",views.for_business,name="for_business"),
    path("about_us",views.about_us,name="about_us"),
    path("submit-income/",views.submit_income,name="submit_income"),
    path("add-expenses/",views.add_expenses,name="add_expenses"),
]
