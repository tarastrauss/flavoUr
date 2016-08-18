from rest_framework import serializers
from menus.models import Menu, Item


class MenuSerializer(serializers.ModelSerializer):

  class Meta:
      model = Menu
      fields = ('id', 'chef', 'title','delivery')

class ItemSerializer(serializers.ModelSerializer):
  menu = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

  class Meta:
      model = Item
      fields = ('id', 'title', 'description', 'price', 'size', 'menu')

