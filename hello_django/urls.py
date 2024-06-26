"""
URL configuration for hello_django project.

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
from django.urls import path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings
include("django.contrib.auth.urls")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('', views.index, name='index'),
    path('reg', views.reg),   
    path('profile', views.profile, name='profile'),
    path('apartcatalog', views.kvartira, name='apartcatalog'),
    path('logout', views.StyledLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('house/<int:house_id>', views.house, name='house'),
    path('apartment/<int:apartment_id>', views.apartment, name='apartment'),
    path('catalog', views.catalog, name='catalog'),  
    path('create/<int:apartment_id>', views.create, name='create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)