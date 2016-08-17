from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from menus.models import Menu, Item
from django.shortcuts import get_object_or_404
from chefs.models import Chef
from django.contrib.auth.decorators import login_required
from simplejson import JSONEncoder
# from django.core import serializers
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


# this stuff doesn't work:
# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         # fields = ('id', 'title', 'delivery', 'chef', 'items')
#         fields=('data', 'message')

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @permission_classes((permissions.AllowAny,))
@login_required
@api_view(['GET', 'POST'])
def menu(request):
    '''
    Restful view for getting or creating a menu
    '''

    print 'hi'
    response = {'message': ''}
    chef = get_object_or_404(Chef, user=request.user)
    menu = Menu.objects.create(chef=chef, title=request.data.title,
                               delivery=request.data.delivery)
    if len(request.data.items) > 0:
      for i in request.data.items:
        item = Item.objects.create(menu=menu, title=i.title, size=i.size, price=i.price,
                                   description=i.description)
    response['data'] = menu.to_dict()
    response['message'] = ('Success. Created instance of the menu class for #%s.'
                                   % menu.title)
    serializer = MenuSerializer(response, many=True)
    # return JSONResponse(serializer.data, status=201)
    # return JsonResponse(serializers.serialize('json', {'key': 'value'}), safe=False)
    return JsonResponse({'key': 'value'})


# this stuff is for the GET request and is going to be in a different function:
    # _menu = get_object_or_404(Menu, id=menu_id)
    # if request.method == 'GET':
    #   response['data'] = _menu.to_dict()
    #   response['message'] = ('Success. Returned data for menu #%s.'
    #                                  % menu_id)
    # elif request.method == 'POST':
