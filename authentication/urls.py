from django.urls import path
from . import views

urlpatterns = [
    path("", views.auth, name="auth_page"),
    path("signup/", views.signin, name="signin"),
    path("signin/", views.signup, name="signup"),
]