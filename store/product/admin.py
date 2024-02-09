from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product"""
    list_display = ("title", "price", "get_description")
    list_display_links = ("title",)
    # readonly_fields = ("created_at", )
    search_fields = ["title"]

    def get_description(self, obj):
        if obj.description:
            return obj.description[:20] + "..." if len(obj.description) > 20 else obj.description[:20]
