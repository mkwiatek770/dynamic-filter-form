from django.core.management.base import BaseCommand
from core.models import Article, Author, Category
from faker import Faker
import datetime
from random import sample, randint

categories = [
    "football",
    "volleyball",
    "politics",
    "mathematics",
    "physics"
]


def add_categories(obj):
    cat_num = randint(1, len(categories))
    for cat_name in sample(categories, cat_num):
        category = Category.objects.get_or_create(
            name=cat_name
        )[0]
        obj.categories.add(category)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("number", type=int,
                            help="Number of articles to create")

    def handle(self, *args, **kwargs):
        faker = Faker()
        for _ in range(kwargs["number"]):
            title = faker.sentence()
            author_name = faker.first_name()
            published_date = faker.date_between()
            reviewed = faker.boolean()

            author = Author.objects.get_or_create(
                name=author_name
            )[0]

            article = Article.objects.create(
                title=title,
                author=author,
                published_date=published_date,
                reviewed=reviewed
            )
            add_categories(article)

        self.stdout.write(self.style.SUCCESS('Articles populated succesfully'))
