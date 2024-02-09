from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('profile/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
