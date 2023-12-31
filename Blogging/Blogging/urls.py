"""Blogging URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from Login.views import restricted_page
from Login import views

urlpatterns = [   
    path('admin/', admin.site.urls),
    path("",views.hone),
    path('Registraion/',views.reg),
    path('Login/',views.login),
    path('food/',views.Food),
    path('about/',views.about),
    path('drink/',views.drink),
    # path('<slug:slug>',views.comment),
     path('food/<slug>/', views.your_view, name='your_view'),
    # path('delete/<int:article_id>/', views.delete, name='delete'),
    path('restaurant/',views.rest),
    path('restaurant/<slug>',views.your_view),
    path('logout/',views.logout),
    path("Admin/", views.Admin, name="Admin Panel"),
    path('table/',views.table,name = "tables"),
    path('restricted/', views.create_article, name='restricted-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
