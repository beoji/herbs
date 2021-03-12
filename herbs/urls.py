from django.contrib import admin
from django.urls import include, path
from catalog.views import account_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('accounts/profile/', account_profile, name='account_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]
