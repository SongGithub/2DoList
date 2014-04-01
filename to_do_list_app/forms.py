import datetime

from django import forms
from django.forms import ModelForm, DateTimeField
# from django.contrib.admin.widgets import AdminDateWidget
from bootstrap3_datetime.widgets import DateTimePicker
from to_do_list_app.models import Item
from to_do_list_app.models import Category

from django.contrib.admin import widgets
# from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form


# form for item management purpose
class ItemForm(ModelForm):
    # Due_date = DateTimeField(widget=AdminDateWidget)
    # Create_date = DateTimeField(widget=AdminDateWidget)
    # Due_date = DateTimeField(widget=SelectDateWidget)
    Due_date = DateTimeField(
        input_formats=['%d-%m-%Y %H:%M'],
        widget=DateTimePicker(
            options={
                "format":"DD-MM-YYYY HH:mm",
                "pickSeconds": False}))
    # Create_date = DateTimeField(widget=SelectDateWidget)
    Create_date = DateTimeField(
        input_formats=['%d-%m-%Y %H:%M'],
        widget=DateTimePicker(
            options={
                "format":"DD-MM-YYYY HH:mm",
                "pickSeconds": False
            }
        )
    )
    Description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3
            }
        )
    )

    CompleteStatus = forms.BooleanField(
        label="Complete Status",
        required=False,

        widget=forms.CheckboxInput(
            attrs={   
                "data-on-text": ' Yes',
                "data-off-text":"NO",
                "data-size": "medium",
                # "disabled":"true"
                "text-lable":"haha",
                "on":'danger',
            }
        )
    )
        


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
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        # self.fields['Description'].widget.attrs['rows'] = 3

# form for add item purpose
class AddItemForm(ModelForm):
    # Due_date = DateTimeField(widget=AdminDateWidget)
    # Due_date = DateTimeField(widget=SelectDateWidget)
    
    Due_date = DateTimeField(input_formats=['%d-%m-%Y %H:%M'],widget=DateTimePicker(options={
    "format":"DD-MM-YYYY HH:mm","pickSeconds": False}))
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
