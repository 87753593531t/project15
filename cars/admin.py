from django.contrib import admin

from cars.models import Car, CarAttachment


class CarAttachmentAdminInLine(admin.StackedInline):
    model = CarAttachment
    extra = 0
    classes = ['collapse']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [
        CarAttachmentAdminInLine,
    ]


