from django.contrib import admin

from printers.models import Printer, PrinterAttachment


class PrinterAttachmentAdminInLine(admin.StackedInline):
    model = PrinterAttachment
    extra = 0
    classes = ['collapse']


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    inlinse = [
        PrinterAttachmentAdminInLine,
    ]
