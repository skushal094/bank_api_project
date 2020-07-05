from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_from_ifsc, name="get_from_ifsc"),
    path('get-branches/', views.get_branches, name="get_branches"),
]
