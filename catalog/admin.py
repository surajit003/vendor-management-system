from django.contrib import admin
from django import forms
from .models import Product, ProductImage, Category


class ProductImagesInline(admin.StackedInline):
    model = ProductImage


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        if self.cleaned_data["price"] <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return self.cleaned_data["price"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "is_active",
    )
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ("name",)
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = (
        "id",
        "name",
        "slug",
        "sku",
    )
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ("name",)
    list_per_page = 20
    inlines = [ProductImagesInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "get_product_name")

    def get_product_name(self, obj):
        return obj.product.name

    get_product_name.short_description = "Product"
