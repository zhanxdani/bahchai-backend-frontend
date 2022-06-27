from django.contrib import admin

# Register your models here.
from .models import Product, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "id")


# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ("name", "category","id")
#     search_fields = ("name", "category__name")
#     list_filter = ("category__name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "is_active",
        "created",
    )
    search_fields = (
        "name",
        "price",
        "category__name",

    )
    list_filter = (
        "category__name",
        "is_active",
        "created",
    )