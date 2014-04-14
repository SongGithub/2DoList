from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from to_do_list_app.models import Category
from to_do_list_app.models import Item
from to_do_list_app.forms import ItemForm
from to_do_list_app.forms import AddItemForm
from to_do_list_app.forms import CategoryForm
from to_do_list_app.forms import AddCategoryForm
from to_do_list_app.forms import markcompleteform


class Category_ListView(generic.ListView):
    model = Category
    template_name = 'to_do_list_app/INDEX_ViewCategories.html'
    context_object_name = 'Cate_List'


class Manage_Category(generic.UpdateView):
    model = Item
    template_name = 'to_do_list_app/ManageCategory.html'
    form_class = CategoryForm

    def get_slug(self):
        return self.kwargs.get('slug')

    def get_queryset(self):
        return Category.objects.filter(slug=self.get_slug())
        # double underscore?

    def get_context_data(self, **kwargs):
        ctx = super(Manage_Category, self).get_context_data(**kwargs)
        #'super'
        ctx['slug'] = self.get_slug()
        return ctx

    def get_success_url(self):
    #generate success url after update button is hit.
        return reverse(
            'Category-summary-view',
            )


class Delete_Category(generic.DeleteView):
    model = Category

    def get_slug(self):
        return self.kwargs.get('slug')

    def get_queryset(self):
        return Category.objects.filter(slug=self.get_slug())
        # double underscore?

    def get_success_url(self):
    #generate success url after update button is hit.
        return reverse(
            'Category-summary-view',
        )


# class Manage_Category(object):
class Add_Category(generic.CreateView):
    model = Category
    template_name = 'to_do_list_app/Add_Category.html'
    form_class=AddCategoryForm

    def get_success_url(self):
    #generate success url after update button is hit.
        return reverse(
            'Category-summary-view',
        )


class Item_perCategory_ListView(generic.ListView):
    model = Item
    template_name = 'to_do_list_app/ItemViewforCategory.html'
    context_object_name = 'Item_List'

    def get_slug(self):
        return self.kwargs.get('slug')

    def get_queryset(self):
        # filter by a given category
        return Item.objects.filter(
            category__slug=self.get_slug()).order_by('-Due_date')

    def get_context_data(self, **kwargs):
        ctx = super(Item_perCategory_ListView, self).get_context_data(**kwargs)
        ctx['slug'] = self.get_slug()
        return ctx


class Add_Item(generic.CreateView):
    model = Item
    template_name = 'to_do_list_app/AddItem.html'
    form_class = AddItemForm

###############for category auto-fill#############################
    def get_category(self):
        return Category.objects.get(slug=self.kwargs.get('slug'))

    def get_form_kwargs(self):
        kwargs = super(Add_Item, self).get_form_kwargs()
        kwargs['category'] = self.get_category()
        return kwargs
##############################################################
    def get_context_data(self, **kwargs):
        ctx = super(Add_Item, self).get_context_data(**kwargs)
        ctx['category'] = self.get_category()
        return ctx

    def get_success_url(self):
    #generate success url after update button is hit.
        return reverse(
            'item-of-category-view',
            kwargs={
                'slug': self.object.category.slug
            }
        )


# class Delete_Item(generic.DeleteView): 
'''when need delete confirmation page, use delect view but not the funcion'''
class Delete_Item(generic.RedirectView):
    model = Item
    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(self.model, slug=kwargs['slug'])
        # item.CompleteStatus = True
        item.delete()

        return reverse(
            'item-of-category-view',
            kwargs={
                'slug': item.category.slug
            }
        )
    def get_success_url(self):
    #generate success url after update button is hit
        return reverse(
            'item-of-category-view',
            kwargs={
                'slug': self.object.category.slug
            }
        )


class Manage_Item(generic.UpdateView):
    model = Item
    template_name = 'to_do_list_app/ManageItem.html'
    form_class = ItemForm

    def get_slug(self):
        return self.kwargs.get('slug')

    # def get_cateslug(self):
    #     return self.kwargs.get('cates')

    def get_queryset(self):
        return Item.objects.filter(slug=self.get_slug())
        # double underscore?

    def get_context_data(self, **kwargs):
        ctx = super(Manage_Item, self).get_context_data(**kwargs)
        #'super'
        ctx['slug'] = self.get_slug()
        # ctx['cates']=self.get_cateslug()
        return ctx

    def get_success_url(self):
    #generate success url after update button is hit.
        return reverse(
            'item-of-category-view',
            kwargs={
                'slug': self.object.category.slug
             }
            )

class MarkItemComplete(generic.RedirectView):
    model = Item
    permanent = False
    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(self.model, slug=kwargs['slug'])
        item.CompleteStatus = True
        item.save()

        return reverse(
            'item-of-category-view',
            kwargs={
                'slug': item.category.slug
            }
        )