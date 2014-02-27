from django.conf.urls import patterns, include, url
from django.contrib import admin
from to_do_list_app import views
admin.autodiscover()
#this give rights to edit in admin page

urlpatterns = patterns('',
                       
                       url(r'^todolist/', include('to_do_list_app.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', 
                        # views.helloworld,
                        views.Category_ListView.as_view(),
                            name='Go-Back-Category-summary-view'),
                      )
