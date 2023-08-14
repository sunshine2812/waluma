"""
URL configuration for walumabank project.

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
from django.urls import path
from customer.views import index,connection,inscription,home
from account_manager.views import connection_manager,show,create_account
from complain.views import add
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/index', index ,name= "index"),
    path('customers/connection', connection ,name= "connection"),
    path('customers/inscription', inscription ,name= "inscription"),
    path('customers/home', home ,name= "home"),
    path('account_managers/', connection_manager ,name= "connection-manager"),
    path('account_managers/show', show ,name= "show"),
    path('account_managers/create_account',create_account, name="inscription-manager"),
    path('complains/', add , name="add"),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer/logout.html'), name='logout'),
    path('logout_manager/', auth_views.LogoutView.as_view(template_name='account_manager/logout.html'), name='logout_manager')

]
