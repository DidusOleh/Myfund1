from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/update_progress", views.update_progress, name="update_progress"),
    path("<int:pk>/donate/", views.donate, name="donate"),
]
