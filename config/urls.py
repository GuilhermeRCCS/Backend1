# Import required libraries
from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the application
urlpatterns = [
    # Include the URL patterns for the admin site and the tasks app
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]