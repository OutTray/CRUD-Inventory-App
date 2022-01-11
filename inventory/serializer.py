from rest_framework import serializers
from .models import Inventory_db

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_db
        fields = '__all__'