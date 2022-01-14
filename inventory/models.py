from django.db import models

# Create your models here.

class Inventory_db(models.Model):
    item_name = models.CharField(max_length = 255)
    item_quantity = models.IntegerField(default = 0)


