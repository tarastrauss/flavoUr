from django.conf.urls import url
from menus import views

urlpatterns = [
    url(r'^menus/$', views.MenuList.as_view()),
    url(r'^menus/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),
    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view())
]


