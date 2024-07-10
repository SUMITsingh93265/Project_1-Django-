"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# This method is from coding school
from vege import views

# Both the is specially for the rendaring images
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Sumit Ice-cream Admin"
admin.site.site_title = "Sumit Ice-cream Admin Portal"
admin.site.index_title = "Welcome to Sumit Ice-cream"
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path("recipes/", views.recipes , name='recipes'),
    path("delete_recipe/<id>/", views.delete_recipe , name='delete_recipe'),
    path("update_recipe/<id>/", views.update_recipe , name='update_recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)