"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from Indrenievents.views import testpage,registrationpage,loginpage,homepage,addeventpage,vieweventpage
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',testpage,name='home'),
    path('register/',registrationpage,name='register'),
    path('login/',loginpage,name='login'),
    path('home/',homepage,name='home'),
    path('addevent/',addeventpage,name='addevent'),
    path('viewevent/',vieweventpage,name='viewevent'),
    path('viewevent/',include('Indrenievents.urls',namespace='Indrenievents'))
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)