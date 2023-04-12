from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplica_compras/', include("aplica_compras.urls")),
]