from django.contrib import admin
from django.urls import path

from accounts.views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserCreateView.as_view())
]
