from django.forms import ModelForm, DateTimeField
from django.contrib.admin.widgets import AdminDateWidget
from to_do_list_app.models import Item
from to_do_list_app.models import Category
import datetime


class ItemForm(ModelForm):
    Due_date=DateTimeField(widget=AdminDateWidget)
    Create_date=DateTimeField(widget=AdminDateWidget)
    
    class Meta:
        model = Item
        fields={'Due_date','Create_date','Name_item','Description','Priority','category','CompleteStatus'}

class AddItemForm(ModelForm):
    Due_date=DateTimeField(widget=AdminDateWidget)
    #WANTED
    # auto define current date, and display on the page
    #auto define current category
    class Meta:
        model = Item
        fields= [
            'Due_date',
            'Name_item',
            'Description',
            'Priority',
            'Create_date',
            'category'
        ]
 

class CategoryForm(ModelForm):
        
    class Meta:
        model = Category
        fields={'Name_category','Description_category'}

class AddCategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields={'Name_category','Description_category'}