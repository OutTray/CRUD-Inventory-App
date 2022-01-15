from django.db import models

# Create your models here.

class Inventory_db(models.Model):
    item_name = models.CharField(max_length = 255, unique = True)
    item_quantity = models.IntegerField(default = 0)


