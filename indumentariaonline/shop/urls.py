from django.urls import path
from . import views

urlpatterns = [
    path("shop/", views.index, name="index"),
    path("shop/contacto", views.contacto, name="contacto"),
    path("shop/nueva-remera", views.nueva_remera, name="nuevaRemera")
]