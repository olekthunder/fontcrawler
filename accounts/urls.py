from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('auth/', views.AuthRedirect.as_view(), name='check-auth'),
    path('edit/', views.update_profile, name='edit'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('log_out/', views.log_out, name='log_out')
]
