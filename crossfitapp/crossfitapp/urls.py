"""crossfitapp URL Configuration

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
from django.urls import path, include
from core.views import info, detail, new, edit, delete

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('info/', info, name="info"),
    path('admin/', admin.site.urls),
    path('new/', new, name='new'),
    path('item/<int:pk>/', detail, name="detail"),
    path('<int:pk>/edit/', edit, name="edit"),
    path('<int:pk>/delete/', delete, name="delete")
]
