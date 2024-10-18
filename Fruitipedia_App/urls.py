
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Fruitipedia_App.common.urls')),
    path('fruit/', include('Fruitipedia_App.fruit.urls')),
    path('profile/', include('Fruitipedia_App.user.urls')),
]
