from django.contrib import admin
from django.urls import path,include
from myapp.views import (
    home,
)
urlpatterns = [
    path('', home,name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
