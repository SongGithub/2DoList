from django.forms import ModelForm, DateTimeField
from django.contrib.admin.widgets import AdminDateWidget
from to_do_list_app.models import Item
from to_do_list_app.models import Category
import datetime
import gettext

from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form


# form for item management purpose
class ItemForm(ModelForm):
    # Due_date = DateTimeField(widget=AdminDateWidget)
    # Create_date = DateTimeField(widget=AdminDateWidget)
    Due_date = DateTimeField(widget=SelectDateWidget)
    Create_date = DateTimeField(widget=SelectDateWidget)

    class Meta:
        model = Item
        fields = [
            'Due_date',
            'Create_date',
            'Name_item',
            'Description',
            'Priority',
            'category',
            'CompleteStatus'
        ]


# form for add item purpose
class AddItemForm(ModelForm):
    # Due_date = DateTimeField(widget=AdminDateWidget)
    Due_date = DateTimeField(widget=SelectDateWidget)
    #WANTED
    # auto define current date, and display on the page
    #auto define current category

##########for category auto-fill###################3
    def __init__(self, category, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)
        self.category = category
        # self.fields['Due_date'].widget = widgets.AdminDateWidget()

    def save(self, force_insert=False, force_update=False, commit=True):
        obj = super(AddItemForm, self).save(commit=False)
        obj.category = self.category
        if commit:
            obj.save()
        return obj
#####################################################

    class Meta:
        model = Item
        fields = [
            'Due_date',
            'Name_item',
            'Description',
            'Priority',
            # 'category',
        ]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'Name_category',
            'Description_category'
        ]


class AddCategoryForm(ModelForm):
        class Meta:
            model = Category
            fields= [
                'Name_category',
                'Description_category'
            ]
