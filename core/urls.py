"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from crypto.views import Coin_Price_View
from product.views import Category_ViewSet, Product_Image_ViewSet, Product_ViewSet

starterURL = 'api/v1/'

urlpatterns = [
    path('modir/', admin.site.urls),  # changed for security
    path(r'' + starterURL+'crypto/',Coin_Price_View.as_view(), name="Coin_Price_View")
]

# ViewSets #############################################################################################################
router = routers.DefaultRouter()
router.register(r'products', Product_ViewSet, )
router.register(r'categories', Category_ViewSet, )
router.register(r'product_images', Product_Image_ViewSet, )

urlpatterns += [
    url(r'' + starterURL, include(router.urls), name='product_url', ),
]

# drf_spectacular ######################################################################################################
urlpatterns += [
    # YOUR PATTERNS
    path(starterURL + 'schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(starterURL + 'schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(starterURL + 'schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
