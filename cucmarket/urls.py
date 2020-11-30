"""cucmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from cart.views import CartInfoViewSet

router1 = routers.DefaultRouter()
router1.register('cart', CartInfoViewSet)
router1.register('goods', CartInfoViewSet)
router1.register('users', CartInfoViewSet)

# router3 = routers.DefaultRouter()
# router3.register('user', CartInfoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('goods.urls')),
    url(r'^user/', include('user.urls')),
    path('api/', include(router1.urls)),
    path("docs/", include_docs_urls(title="DRF API文档", description="Django REST framework快速入门")),
]
