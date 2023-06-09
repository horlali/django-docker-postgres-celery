import os

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Diagnosis Backend",
        default_version="1.0",
        description="Diagnosis Backend API Collection",
        contact=openapi.Contact(email=os.getenv("DEV_CONTACT", "email@example.com")),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

API_VERSION = "api/v1"

urlpatterns = [
    path(
        "",
        schema_view.with_ui(
            "swagger",
            cache_timeout=0,
        ),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path(f"{API_VERSION}/icd/", include("icd.urls")),
]
