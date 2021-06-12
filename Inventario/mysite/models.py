from django.db import models

# Create your models here.

class product(models.Model):
    product_code = models.CharField(max_length= 5 , unique=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1, null= True, blank= True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name