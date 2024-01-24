from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='list'),
    path('<str:title>', views.DetailView.as_view(), name='list'),
    
]