from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('create-resume', views.create_resume, name="create-resume"),
    path("resume", views.resume, name="resume")
]