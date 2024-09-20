"""
URL configuration for kronaclub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

# from users.views import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'rest-auth/', include('rest_auth.urls'))
    # path('oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    # path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('oauth2/', include('oauth2_provider.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),

    # path('oauth2/', include(oauth2_provider.urls)),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/', include('api_v1.urls')),
]
# curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=slepcovolezhka@gmail.com&password=olegoleg'
# curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=slepcovolezhka&password=olegoleg'

