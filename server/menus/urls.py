from django.conf.urls import url
from menus import views

urlpatterns = [
    url(r'^menu_root/(?P<pk>[0-9]+)/$', views.menu_root.as_view(), name="menu-root"),
    url(r'^menu_root/$', views.menu_root.as_view(), name="menu-root"),
    url(r'^menus/$', views.MenuList.as_view(), name="menu-list"),
    url(r'^menu/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view(), name="menu-detail"),
    url(r'^menu/(?P<pk>[0-9]+)/items$', views.ItemList.as_view(), name="item-list"),
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view(), name="item-detail")
]


