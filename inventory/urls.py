from django.contrib import admin
from django.urls import path
from inventory import views
from .api import InventoryCreateApi, InventoryApi, InventoryUpdateApi, InventoryDeleteApi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create", views.create),
    path("show", views.show),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete),

    path('api', InventoryApi.as_view()),
    path('api/create', InventoryCreateApi.as_view()),
    path('api/<int:pk>', InventoryUpdateApi.as_view()),
    path('api/<int:pk>/delete', InventoryDeleteApi.as_view()),
]