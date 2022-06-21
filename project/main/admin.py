from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "price_usd", "price_rub", "delivery_date"]
    readonly_fields = ["price_rub"]
    date_hierarchy = "delivery_date"


admin.site.register(Order, OrderAdmin)
