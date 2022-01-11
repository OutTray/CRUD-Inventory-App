from django.urls import path
from .api import InventoryCreateApi, InventoryApi, InventoryUpdateApi, InventoryDeleteApi

urlpatterns = [
    path('api', InventoryApi.as_view()),
    path('api/create', InventoryCreateApi.as_view()),
    path('api/<int:pk>', InventoryUpdateApi.as_view()),
    path('api/<int:pk>/delete', InventoryDeleteApi.as_view()),
]