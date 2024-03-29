"""bid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log&reg/',TemplateView.as_view(template_name="user_templates/log&reg.html"),name="log&reg"),
    path('user_home1/',TemplateView.as_view(template_name="user_templates/user_home.html"),name="user_home1"),
    path('savedetails/',views.saveDetails,name="savedetails"),
    path('user_home/',views.user_home,name="user_home"),
    path('sellproduct/',TemplateView.as_view(template_name="user_templates/sellproduct.html"),name="sellproduct"),
    path('saveselldetails/',views.saveSellDetails,name="saveselldetails"),
    path('bid_product/',views.bidProduct,name="bid_product"),
    path('displayproduct/',views.displayProduct,name="displayproduct"),
    path('logout/',views.logout,name="logout")
]
