from django.conf.urls import patterns, include, url
from django.contrib import admin
from to_do_list_app import views
from django.shortcuts import redirect

<<<<<<< HEAD
urlpatterns = patterns('',
                       url(r'^index/managecategory/$',
                           views.Add_Category.as_view(),
                           name="managecategory"),
                       url(r'^index/$',
                           views.Category_ListView.as_view(),
                           name='Category-summary-view'),
                       url(r'^view-items-of-category/(?P<slug>[\w-]+)/Add/$',
                           views.Add_Item.as_view(), name="Add_Item"),
                       url(r'^view-items-of-category/(?P<slug>[\w-]+)/Back/$',
                           views.Category_ListView.as_view(),
                           name='Go-Back-Category-summary-view'),
                       url(r'^view-items-of-category/(?P<slug>[\w-]+)/$',
                           views.Item_perCategory_ListView.as_view(),
                           name='item-of-category-view'),
                       url(r'^manage-item-of/(?P<slug>[\w-]+)/Delete/$',
                           views.Delete_Item.as_view(), name="Delete_Item"),
                       url(r'^manage-category-of/(?P<slug>[\w-]+)/Delete/$',
                           views.Delete_Category.as_view(),
                           name="Delete_Category"),
                       url(r'^manage-item-of/(?P<slug>[\w-]+)/$',
                           views.Manage_Item.as_view(), name="manage-item"),
                       url(r'^manage-category-of/(?P<slug>[\w-]+)/$',
                           views.Manage_Category.as_view(),
                           name="manage-category-of"),
                       )
=======
(r'^favicon\.ico$', 
'django.views.generic.simple.redirect_to', 
{'url': '/media/favicon.ico'}),

urlpatterns = patterns(
    '',
    url(
        r'^index/managecategory/$',
        views.Add_Category.as_view(),
        name="managecategory"
        ),
    url(r'^index/$',
       views.Category_ListView.as_view(),
       name='Category-summary-view'),
    url(r'^view-items-of-category/(?P<slug>[\w-]+)/Add',
       views.Add_Item.as_view(), name="Add_Item"),
    url(r'^view-items-of-category/(?P<slug>[\w-]+)/Back',
       views.Category_ListView.as_view(),
       name='Go-Back-Category-summary-view'),
    url(r'^view-items-of-category/(?P<slug>[\w-]+)/$',
       views.Item_perCategory_ListView.as_view(),
       name='item-of-category-view'),
    url(r'^manage-item-of/(?P<slug>[\w-]+)/Delete/$',
       views.Delete_Item.as_view(), name="Delete_Item"),
    url(r'^manage-category-of/(?P<slug>[\w-]+)/Delete/$',
       views.Delete_Category.as_view(),
       name="Delete_Category"),
    url(r'^manage-item-of/(?P<slug>[\w-]+)/$',
       views.Manage_Item.as_view(), name="manage-item"),
    url(r'^manage-category-of/(?P<slug>[\w-]+)/$',
       views.Manage_Category.as_view(),
       name="manage-category-of"),
    url(r'',
       views.Category_ListView.as_view(),
       name='Category-summary-view'),
)


# /
# /<category_slug>/
# /<category_slug>/add/
# /<category_slug>/delete/
# /<category_slug>/edit/
# /<category_slug>/<item_slug>/
# /<category_slug>/<item_slug>/add/
# /<category_slug>/<item_slug>/delete/
# /<category_slug>/<item_slug>/edit/

# REST API
# --------

# GET A LIST OF categories

#   GET /categories/

# CREATE NEW
#   POST /categories/ 

# Fetch

#   GET /categories/<slug>/

# Delete

#   DELETE /categories/<slug>/

# UPDATE

#   PUT /categories/<slug>/
>>>>>>> cdd3ff54bd4100e5f45d889c825b1d236b6b48fd
