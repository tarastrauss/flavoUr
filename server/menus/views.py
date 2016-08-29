from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from menus.models import Menu, Item
from menus.serializers import MenuSerializer, ItemSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import viewsets

class menu_root(APIView):

  def get(self, request, *args, **kwargs):
    menu_view = MenuDetail.as_view()
    items_view = ItemList.as_view()
    return Response({
        'Menu': menu_view(request, *args, **kwargs).data,
        'Items': items_view(request, *args, **kwargs).data
    })

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
      menu = Menu.objects.get(pk=self.kwargs['pk'])
      serializer.save(menu=menu)

    def get_queryset(self):
      menu_pk = self.kwargs['pk']
      return Item.objects.filter(menu__pk=menu_pk)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
      menu_pk = self.kwargs['menu_pk']
      item_pk = self.kwargs['pk']
      return Item.objects.filter(menu__pk=menu_pk, pk=item_pk)
