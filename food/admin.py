from django.contrib import admin

from .models import Cuisine,Food,Order
# Register your models here.

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('category','created_at')
    search_fields=('category',)
    ordering=('category',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','price','is_avaliable')
    search_fields=('name',)
    list_editable=('is_avaliable',)
    list_filter=('is_avaliable',)
    ordering=('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','user','order_details','is_ready','is_delivered')
    list_editable=('is_ready','is_delivered')
    ordering=('-id',)

admin.site.register(Cuisine,CuisineAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Order,OrderAdmin)