from django.contrib import admin
from .models import Category,Product,CartItem,Cart
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)