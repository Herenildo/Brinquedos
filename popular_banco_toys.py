import os, django
import faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from apps.toys.models import Toy
from django.utils import timezone

toy_names = ['Action Figure', 'Barbie Doll', 'Lego Set', 'Hot Wheels Car', 'Board Game', 
             'Teddy Bear', 'Kids Drone', 'Race Car Track', 'Puzzle', 'Playmobil Set', 
             'Toy Robot', 'Water Gun', 'Stuffed Animal', 'Building Blocks', 'Rubik\'s Cube', 
             'Toy Train', 'Yo-Yo', 'Remote Control Car', 'Slinky', 'Play-Doh']

category = ['Action Figure', 'Puzzle', 'Doll', 'Board Game', 'Electronic Toy', 'Outdoor Toy']

def creating_toys(quantity_of_toys):
    fake=Faker('en_US')
    for _ in range(quantity_of_toys):
        created_naive = fake.date_time()
        created =timezone.make_aware(created_naive)
        name = fake.random_element(elements=toy_names)
        description = fake.text()
        toy_category= fake.random_element(elements=category)
        release_date = fake.date_time()
        was_include_in_home = fake.boolean()
        p = Toy(created=created, name=name, description=description,toy_category=toy_category,release_date=release_date, was_include_in_home=was_include_in_home)
        p.save()

creating_toys(50)