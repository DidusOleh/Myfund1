from django.contrib.auth import views as auth_views
from django.contrib.auth import views as authViews
from django.urls import path
from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path('exit/', authViews.LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
]
