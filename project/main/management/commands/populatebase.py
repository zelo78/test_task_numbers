import random

from django.core.management.base import BaseCommand

from main.models import User, Post
from main.factories import (
    UserFactory,
    PostFactory,
)


class Command(BaseCommand):
    help = "Populate DB with a few Users and Posts for testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            nargs="?",
            default=25,
            type=int,
            help="Count of Post to be created, default 25",
        )

    def handle(self, *args, **options):
        count = options["count"]

        # мы добавим count сообщений, но прочих объектов в базе должно быть >= half
        half = max(10, count // 2)

        for model, model_factory, target_count in (
            (User, UserFactory, half),
            (Post, PostFactory, count),
        ):
            current_count = model.objects.count()
            if current_count < target_count:
                model_factory.create_batch(target_count - current_count)

        # sellers = Seller.objects.all()
        # categories = Category.objects.all()
        # tags = Tag.objects.all()
        # for i in range(count):
        #     seller = random.choice(sellers)
        #     category = random.choice(categories)
        #     ad = AdFactory.create(seller=seller, category=category)
        #     for tag in random.sample(list(tags), k=random.randint(0, 5)):
        #         ad.tags.add(tag)
        #     if i % 10 == 0:
        #         ad.archived = True
        #     self.stdout.write(f'Ad {ad} ads was created')
        #
        # self.stdout.write(f'{count} ads was created')
