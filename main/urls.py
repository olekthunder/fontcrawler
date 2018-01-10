from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.HomeRedirect.as_view()),
    path('home/', views.home, name='home'),
    path('fonts/', views.FontListView.as_view(), name='fonts'),
    path('add_font/', views.add_font, name='add_font'),
    path('about/', views.AboutView.as_view(), name='about')
]
