from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from menus.models import Menu, Item
from menus.serializers import MenuSerializer, ItemSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework import permissions

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.menu)

class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
