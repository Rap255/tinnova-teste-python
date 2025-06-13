from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Tinnova Veiculos",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/',include('vehicles.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)