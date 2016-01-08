from django.conf.urls import include, url
from django.contrib import admin

from inventory import views
from contact import views as contact_view

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items_list/', views.items_list, name='items_list'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^items_pagination/', views.items_pagination, name='items_pagination'),
    url(r'^contact/$', contact_view.contact, name='contact'),
    # Admin area
    url(r'^admin/', include(admin.site.urls)),
]
