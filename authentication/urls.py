from django.urls import path
from . import views

urlpatterns = [
    path("", views.auth, name="auth_page"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
]