from random import choice

import factory
import factory.fuzzy

from main.models import User, Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    class Params:
        full_name = factory.Faker("name")

    first_name = factory.LazyAttribute(lambda obj: obj.full_name.split(sep=" ")[0])
    last_name = factory.LazyAttribute(lambda obj: obj.full_name.split(sep=" ")[-1])
    email = factory.Faker("email")
    password = factory.Faker("password")

    username = factory.Sequence(lambda n: f"Test_username_{n}")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=5, locale="ru_RU")
    text = factory.Faker("paragraph", nb_sentences=5, locale="ru_RU")
    author = factory.LazyFunction(lambda: choice(User.objects.all()))
