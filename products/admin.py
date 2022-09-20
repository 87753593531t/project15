from django.contrib import admin

from products.models import Product, ProductAttachment


class ProductAttachmentAdminInLine(admin.StackedInline):
    model = ProductAttachment
    extra = 0
    classes = ['collapse']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductAttachmentAdminInLine,
    ]

