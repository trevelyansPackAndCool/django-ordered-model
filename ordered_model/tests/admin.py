from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import Item

class ItemAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

admin.site.register(Item, ItemAdmin)

class PizzaToppingsThroughModelInline(OrderedTabularInline):
    model = PizzaToppingsThroughModel
    fields = ('topping', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    extra = 1
    ordering = ('order',)
