from django.urls import path
from .import views

urlpatterns = [
    path("CartView",views.CartView,name="CartView")
]
