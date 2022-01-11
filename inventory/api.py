from rest_framework import generics
from rest_framework.response import Response
from .serializer import InventorySerializer
from .models import Inventory_db

class InventoryApi(generics.ListAPIView):
    queryset = Inventory_db.objects.all()
    serializer_class = InventorySerializer

class InventoryCreateApi(generics.CreateAPIView):
    queryset = Inventory_db.objects.all()
    serializer_class = InventorySerializer

class InventoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Inventory_db.objects.all()
    serializer_class = InventorySerializer

class InventoryDeleteApi(generics.DestroyAPIView):    
    queryset = Inventory_db.objects.all()
    serializer_class = InventorySerializer
