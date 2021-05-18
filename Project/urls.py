from django.urls import path
from . import views

app_name = "Project"


urlpatterns = [
    path("", views.project, name="project"),
    path("<int:Project_id>/", views.detail, name="detail"),
]

