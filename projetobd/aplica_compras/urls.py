from django.urls import path
from . import views

urlpatterns = [
    path("", views.aplica_compras, name="aplica_compras"),
]