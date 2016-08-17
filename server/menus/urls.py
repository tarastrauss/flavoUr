from django.conf.urls import url
from menus import views

urlpatterns = [
  # url(r'^$', views.menus, name='menus'),
  url(r'^menu/$', views.menu, name='menu_post'),
]
