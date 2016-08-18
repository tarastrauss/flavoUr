from rest_framework import serializers
from menus.models import Menu, Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'price', 'size', 'menu')

class MenuSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = Menu
        fields = ('id','chef','title','delivery','items')
