"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webbrowser import get
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path, include
from smartphone.views import (
    delete_product,
    home,
    get_products,
    add_product,
    delete_product,
    get_products_by_company,
    get_products_by_RAM,
    get_products_by_memory

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('products/', get_products),
    path('add_product/', add_product),
    path('delete_product/<int:id>',delete_product),
    path('products/company/<str:company>', get_products_by_company),
    path('products/ram/<str:RAM>', get_products_by_RAM),
    path('products/memory/<str:memory>', get_products_by_memory)
]
