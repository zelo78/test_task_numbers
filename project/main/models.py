from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    order_id = models.PositiveIntegerField("заказ №", unique=True)
    price_usd = models.FloatField("стоимость, $", default=0)
    price_rub = models.FloatField("стоимость, руб.", default=0)
    delivery_date = models.DateField("срок поставки")

    def __str__(self):
        return f"Заказ #{self.order_id} стоимость {self.price_usd}$"
