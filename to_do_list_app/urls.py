from django.conf.urls import patterns, include, url
from django.contrib import admin
from to_do_list_app import views
from django.shortcuts import redirect


urlpatterns = patterns('',
                       

                       url(r'^index/$',
                           views.Category_ListView.as_view(),
                           name='Category-summary-view'),                    
                       url(r'^category/add',
                           views.Add_Category.as_view(),
                           name="managecategory"),                   
                       url(r'^(?P<slug>[\w-]+)/edit',
                           views.Manage_Category.as_view(),
                           name="manage-category-of"),                   
                       url(r'^(?P<slug>[\w-]+)/Delete',
                           views.Delete_Category.as_view(),
                           name="Delete_Category"),                                         
                       url(r'^(?P<slug>[\w-]+)/$',
                           views.Item_perCategory_ListView.as_view(),
                           name='item-of-category-view'),
                       
                       url(r'^(?P<slug>[\w-]+)/Add',
                           views.Add_Item.as_view(), name="Add_Item"),
#slug for category needed for 'manage':
                       url(r'^(?P<cateslug>[\w-]+)/(?P<slug>[\w-]+)/Manage',
                           views.Manage_Item.as_view(), name="manage-item"),
                       
                       # url(r'^(?P<slug>[\w-]+)/Back/$',
                       #     views.Category_ListView.as_view(),
                       #     name='Go-Back-Category-summary-view'),
                       
                       url(r'^manage-item-of/(?P<slug>[\w-]+)/Delete/$',
                           views.Delete_Item.as_view(), name="Delete_Item"),
                    
                       url(r'^manage-item-of/(?P<slug>[\w-]+)/mark/$',
                           views.MarkItemComplete.as_view(),
                           name="mark-item"),
                       url(r'',
                          views.Category_ListView.as_view(),
                           name='Category-summary-view'),
                       )
                       

#Under renovation since 14Apr

# 'URL layout design guide'
# /<category_slug>/
# /<category_slug>/add/
# /<category_slug>/delete/
# /<category_slug>/edit/
# /<category_slug>/<item_slug>/
# /<category_slug>/<item_slug>/add/
# /<category_slug>/<item_slug>/delete/
# /<category_slug>/<item_slug>/Manage/
