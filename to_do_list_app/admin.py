from django.contrib import admin

# Register your models here.
from to_do_list_app.models import Category
from to_do_list_app.models import Item


class ItemInLine(admin.TabularInline):
#Tabled way of ordering
    model = Item
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['Name_category']}),
        ('What is it about', {'fields': ['Description_category']})
        ]
    inlines = [ItemInLine]
    list_display = (
        'Name_category',
        'Description_category')
    # list_filter=['Due_date']
    search_fields = ['Name_category']

admin.site.register(Category, CategoryAdmin)


# class CategoryAdmin(admin.ModelAdmin) :
#   fields = ['Name_category','Description_category','poll']
# admin.site.register(Category, CategoryAdmin)


####################
###The Easy way#####
####################
# admin.site.register(Item)
#admin.site.register(Category)

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'Name_item',
        'category',
        'Priority',
        'Due_date',
        'CompleteStatus',
        )
admin.site.register(Item, ItemAdmin)
