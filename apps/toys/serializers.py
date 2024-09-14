from dataclasses import fields
from  rest_framework import serializers
from apps.toys.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model =Toy
        fields= (
            'id',
            'name',
            'description',
            'release_date',
            'toy_category',
            'was_include_in_home'
        )

