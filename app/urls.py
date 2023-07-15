"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework import routers


from shop.views import ProductApiList, ProductAPIDestroy, ProductApiUpdate

router = routers.SimpleRouter()

# router.register(r'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/product/', ProductApiList.as_view()),
    path('api/product/<int:pk>/', ProductApiUpdate.as_view()),
    path('api/product/<int:pk>/', ProductAPIDestroy.as_view()),

    path('api/category/', ProductApiList.as_view()),
    path('api/category/<int:pk>/', ProductApiUpdate.as_view()),
    path('api/category/<int:pk>/', ProductAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


    # Самый элегантный способ
    # path('api/', include(router.urls))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
