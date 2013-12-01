from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ToDo.views.list_tasks'),
    url(r'^list_tasks$', 'ToDo.views.list_tasks'),
    url(r'^add_task$', 'ToDo.views.add_task'),
    url(r'^update_task$', 'ToDo.views.update_task'),

)
