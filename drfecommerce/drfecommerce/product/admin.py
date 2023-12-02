from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]    

admin.site.register(ProductLine)
admin.site.register(Brand)
admin.site.register(Category)
