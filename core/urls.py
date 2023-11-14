from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path('exit/', auth_views.LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path("login/",auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm),name="login"),
    path("about/", views.about, name="about"),
    path("term_of_use/", views.term_of_use, name="term_of_use"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
]
