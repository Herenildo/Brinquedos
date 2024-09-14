import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.drones.models import DronesCategory

category = [
    ('Drones de rotor único'),
    ('Drones multirrotores'),
    ('Drones de asa fixa'),
    
]

def  create_category():
    for name in category:
        DronesCategory.objects.create(name=name)

create_category()