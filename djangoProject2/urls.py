"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Clas
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from application import views
from django.urls import include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import  get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   # validators=['flex', 'ssv'],
   public=True,
   # permission_classes=(permissions.AllowAny,),#
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/humen/', views.Human.as_view()),
    path('api/humen/<int:id>/', views.PersonDetail.as_view()),
    path('api/projects/', include("projects.urls")),
    path('api/users/', include("users.urls")),
    path('api/param/', include("param_app.urls")),
    path('api/page/', include("pageapp.urls")),
    path('docs/', include_docs_urls(title="文档", description="i love you")),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
