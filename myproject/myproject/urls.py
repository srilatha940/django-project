"""
URL configuration for myproject project.

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
from django.urls import path
from basic.views import sample   #in basic app in views file we wrote a sample function
from basic.views import sample1
# from basic.views import sampleInfo
from basic.views import sample2
from basic.views import dynamicResponse
from basic.views import addition

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',sample),    # calling a function through views
    path('54R/',sample1),
    # path('info',sampleInfo),
    path('info2',sample2),
    # path('dynamic/',dynamicResponse,name='dynamicResponse')
    path('add',addition,name="addition")
]
