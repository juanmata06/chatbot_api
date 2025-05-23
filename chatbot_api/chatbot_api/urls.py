"""
URL configuration for chatbot_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# General imports:
from django.contrib import admin
from django.urls import include, path
# Drfyasg config imports:
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
      title="Chatbot API",
      default_version='v1',
      description="This is a very basic example of a documentation for an API connected to Chat GPT, used it as a chat bot.",
      contact=openapi.Contact(email="juanmataguzzo17@gmail.com"),
      license=openapi.License(name="BSD License"),
  ),
  public=True,
  #permission_classes=(permissions.AllowAny),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('open_ai.api.router')),
    path('api/', include('user.api.router'))
]
