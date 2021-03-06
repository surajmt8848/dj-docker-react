"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from .views import IndexTemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls", namespace="accounts")),
    path("api/", include('products.urls', namespace='products')),
    path("api/", include('orders.urls', namespace='orders')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
    # path('', index, name='index'),
]  

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   