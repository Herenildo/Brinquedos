from re import M
from tkinter import CASCADE
from django.db import models


class DronesCategory(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Drone(models.Model):
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(DronesCategory, related_name='drones', on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
    
class Pilote(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default='M')
    races_count = models.IntegerField()
    insertinserted_timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
    
class Competition(models.Model):
    pilot = models.ForeignKey(Pilote,related_name='competitions', on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone,on_delete = models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()
    class Meta:
        ordering = ('-distance_in_feet',)
