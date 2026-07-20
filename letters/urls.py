from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='letters/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #የይለፍ ቃል መቀየሪያ URL
    path('change-password/', 
         auth_views.PasswordChangeView.as_view(
             template_name='letters/change_password.html',
             success_url='/'
         ), 
         name='password_change'),
    path('create/', views.create_letter, name='create_letter'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('change-password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('letters/edit/<int:letter_id>/', views.edit_letter, name='edit_letter'),
    path('letters/delete/<int:letter_id>/', views.delete_letter, name='delete_letter'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)