from datetime import timedelta

from django.utils import timezone

import factory
import factory.fuzzy

from main.models import Order


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    order_id = factory.fuzzy.FuzzyInteger(100000, 999999)
    price_usd = factory.fuzzy.FuzzyInteger(1, 1000000)
    price_rub = factory.LazyAttribute(lambda obj: obj.price_usd * 75)
    delivery_date = factory.fuzzy.FuzzyDateTime(
        start_dt=timezone.now(), end_dt=timezone.now() + timedelta(days=720)
    )
