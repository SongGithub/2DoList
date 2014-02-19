from django.db import models
from django.utils import timezone
import datetime



class Category(models.Model):
    Name_category=models.CharField(max_length=20)
    Description_category=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.Name_category

class Item(models.Model):
    category=models.ForeignKey(Category, related_name="Item_set")
    
    Name_item=models.CharField(max_length=20)
    Description=models.CharField(max_length=100)

    Create_date=models.DateTimeField('date created')
    Due_date=models.DateTimeField('date due')

    Priority=models.IntegerField(default=0)
    CompleteStatus=models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.Name_item

    



