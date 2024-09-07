from django.urls import path
from . import views

urlpatterns = [
    path('get-details/', views.get_details, name='get_method'),
]