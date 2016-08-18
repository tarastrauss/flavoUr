from django.contrib import admin
from menus.models import Menu, Item
# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Menu, ItemAdmin)
