from django.shortcuts import render, redirect
from .forms import Inventory_db_Form
from .models import Inventory_db
from django.http import HttpResponse
import csv

# Create your views here.

def create(request):
    if request.method == "POST":
        form = Inventory_db_Form(request.POST)
        if form.is_valid():

            try:
                form.save()
                return redirect("/inventory/show")

            except:
                pass

    else:
        form = Inventory_db_Form()
    
    return render(request, "create.html", {"form": form})

def show(request):
    inventory_selection = Inventory_db.objects.all()

    return render(request, "show.html", {"inventory_selection": inventory_selection})

def update(request, id):
    inventory_selection = Inventory_db.objects.get(id = id)

    form = Inventory_db_Form(request.POST, instance = inventory_selection)

    if form.is_valid():
        form.save()
        return redirect("/inventory/show")
    
    return render(request, "update.html", {"inventory_selection": inventory_selection})

def delete(request, id):
    inventory_selection = Inventory_db.objects.get(id = id)
    inventory_selection.delete()
    return redirect("/inventory/show")

def read(request, id):
    inventory_selection = Inventory_db.objects.get(id = id)
    return render(request, "read.html", {"inventory_selection": inventory_selection})

def csv_all(request):
    inventory_selection = Inventory_db.objects.all()

    response = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment; filename="all_inventory.csv"'}
    )

    field_names = ["id", "item_name", "item_quantity"]

    writer = csv.writer(response)

    writer.writerow(field_names)

    for row in inventory_selection:
        row_values = []
        for field in field_names:
            value = getattr(row, field)
            row_values.append(value)
        writer.writerow(row_values)

    return response

def csv_single(request, id):

    inventory_selection = Inventory_db.objects.get(id = id)

    response = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': f'attachment; filename="{inventory_selection.item_name}_id_{id}_details.csv"'}
    )

    field_names = ["id", "item_name", "item_quantity"]

    writer = csv.writer(response)

    writer.writerow(field_names)

    row_values = []
    for field in field_names:
        value = getattr(inventory_selection, field)
        row_values.append(value)
    writer.writerow(row_values)

    return response