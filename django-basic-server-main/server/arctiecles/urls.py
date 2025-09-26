from django.urls import path
from .views import (
    ArctiecleListView, ArctiecleDetailView,
    ArctiecleCreateView, ArctiecleUpdateView, ArctiecleDeleteView,
)


urlpatterns = [
    path("", ArctiecleListView.as_view(), name="arctiecle-list"),
    path("<int:pk>/", ArctiecleDetailView.as_view(), name="arctiecle-detail"),
    path("create/", ArctiecleCreateView.as_view(), name="arctiecle-create"),
    path("<int:pk>/update/", ArctiecleUpdateView.as_view(), name="arctiecle-update"),
    path("<int:pk>/delete/", ArctiecleDeleteView.as_view(), name="arctiecle-delete"),
]