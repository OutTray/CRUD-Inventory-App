from django import forms
from inventory.models import Inventory_db

class Inventory_db_Form(forms.ModelForm):
    class Meta:
        model = Inventory_db
        fields = "__all__"