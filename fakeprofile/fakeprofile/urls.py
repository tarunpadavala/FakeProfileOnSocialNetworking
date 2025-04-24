"""fakeprofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import get_csrf_token
from .views import predict
from .views import get_profile_info
from .views import FaceBookPredict
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('get-csrf-token/',get_csrf_token,name='get-token'),
    path('twitter/predict/',predict,name='tw-predict'),
    path('instagram/predict/',get_profile_info,name='insta-predict'),
    path('facebook/predict/',FaceBookPredict,name="facebook-predict")
    
]
