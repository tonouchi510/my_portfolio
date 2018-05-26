from django.urls import path
from . import views
from django.views.generic import RedirectView


app_name = 'index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ComingSoon', views.ComingSoon, name='ComingSoon'),
]
