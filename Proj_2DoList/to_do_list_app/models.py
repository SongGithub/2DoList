from django.db import models

class Item(models.Model):
    Name_item=models.CharField(max_length=20)
    Discription=models.CharField(max_length=100)

    Create_date=models.DateTimeField('date created')
    Due_date=models.DateTimeField('date due')

    Priority=models.IntegerField(default=0)
    def __unicode__(self):
        return self.Name_item




class Category(models.Model):
    Name_item=models.CharField(max_length=20)
    Discription=models.CharField(max_length=100)

