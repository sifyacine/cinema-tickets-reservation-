from django.contrib import admin
from django.urls import path, include  # Import the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include URL patterns from users app
]
