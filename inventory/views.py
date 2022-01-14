from django.shortcuts import render, redirect
from .forms import Inventory_db_Form
from .models import Inventory_db

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
    
    return render(request, "index.html", {"form": form})

def show(request):
    inventory_selection = Inventory_db.objects.all()

    return render(request, "show.html", {"inventory_selection": inventory_selection})

def edit(request, id):
    inventory_selection = Inventory_db.objects.get(id = id)
    return render(request, "edit.html", {"inventory_selection": inventory_selection})

def update(request, id):
    inventory_selection = Inventory_db.objects.get(id = id)

    form = Inventory_db_Form(request.POST, instance = inventory_selection)

    if form.is_valid():
        form.save()
        return redirect("/inventory/show")
    
    return render(request, "edit.html", {"inventory_selection": inventory_selection})

def delete(request, id):
    inventory_selection = Inventory_db.objects.get(id = id)
    inventory_selection.delete()
    return redirect("/inventory/show")