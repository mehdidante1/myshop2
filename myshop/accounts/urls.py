from django.urls import path
from .views import SignupView , LoginView , Gg , logout , reset_password , edit_profile 
from django.contrib.auth.views import PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView 
from .forms import *
urlpatterns = [
    path('login/' , LoginView , name = 'login'),
    path('gg/' , Gg , name = 'gg'),
    #path('reset_password/' , reset_password , name = 'reset_password'),
    path('logout/', logout, name = 'logout'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('register/',SignupView , name = 'register'),
    
    path('password_reset/',
         PasswordResetView.as_view(
                template_name = 'accounts/reset_password.html',
                form_class = MyPassResetForm
         ), 
         name='password_reset'),
    
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
                template_name = 'accounts/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
                template_name = 'accounts/password_reset_confirm.html',
                form_class = MySetPassForm
         ), 
         name='password_reset_confirm'),
    

    path('password_reset/complete',
         PasswordResetCompleteView.as_view(
                template_name = 'accounts/password_reset_complete.html'
         ), 
         name='password_reset_complete')
]
