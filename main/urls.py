# app urls

from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('stocks/<slug:stock_slug>/', v.stock)
]