from rest_framework import serializers

from .models import Inventory_db

class Inventory_db_Serializer(serializers.ModelSerializer):
    item_name = serializers.CharField(max_length = 255)
    item_quantity = serializers.IntegerField(default = 0)

    class Meta:
        model = Inventory_db
        fields = ('__all__')