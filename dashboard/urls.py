from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:pk>/", views.userEdit, name="edit"),
]
