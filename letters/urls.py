from django.urls import path
from . import views

urlpatterns = [
    # ዋናው ገፃችን (Home page) ዳሽቦርዱ እንዲሆን እናደርጋለን
    path('', views.dashboard, name='dashboard'),
]