from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create", views.create),
    path("show", views.show),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete),
    path("read/<int:id>", views.read),

    path("all_inventory_csv", views.csv_all, name = "all_inventory_csv"),
    path("item_csv/<int:id>", views.csv_single, name = "item_csv"),
]