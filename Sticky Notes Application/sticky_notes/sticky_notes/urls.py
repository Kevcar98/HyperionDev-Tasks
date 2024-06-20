"""
This is the main URL configuration for the Django project.

It includes:
- The admin site at /admin/
- The notes app at the root URL (/)

Each Django app should have its own URLs module which gets included here.
"""

from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]
