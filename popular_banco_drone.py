import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.drones.models import Drone


dados = [
    ('Blade Chroma Quadcopter Drone'),
    ('Sim Too Pro'),
    ('DJI Phatom 4'),
    ('DJI Mavic Pro'),
    ('DJI Inspire 2'),
    ('Parrot Bebop 2'),
    ('DJI Phantom 3 Standard'),
    ('DJI Phantom 3 Pro'),
    ('3DR Solo'),
    ('Yuneec Q500+')
]

'''
 name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(DronesCategory, related_name='drones', on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)'''