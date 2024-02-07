from django.contrib import admin

# Register your models here.
from product.models import Color, Product, Category, ProductImage, Price, Size


class SizeInline(admin.TabularInline):
    model = Size


class ColorInline(admin.TabularInline):
    model = Color


class PriceInline(admin.TabularInline):
    model = Price


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title', 'slug']
    search_fields = ["title"]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title', 'slug']
    search_fields = ['title', 'category__title']
    inlines = [SizeInline, ColorInline, PriceInline, ProductImageInline]
    autocomplete_fields = ['category']


@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    list_display_links = ['id', 'product', 'image']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs


@admin.register(Price)
class AdminPrice(admin.ModelAdmin):
    list_display = ['id', 'product', 'price', 'count']
    search_fields = ['size__title', 'color__title', 'product_title']
    list_display_links = ['id', 'product', 'price', 'count']
    list_filter = ['size', 'color', 'price', 'count']
    autocomplete_fields = ['size', 'color', 'product']
    inlines = [ProductImageInline]


@admin.register(Size)
class AdminSize(admin.ModelAdmin):
    list_display = ['id', 'product', 'title']
    list_display_links = ['id', 'product', 'title']
    search_fields = ['title']


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ['id', 'product']
    list_display_links = ['id', 'product']
    search_fields = ['title']
