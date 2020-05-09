from .models import List
from rest_framework import serializers


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['name', 'owner', 'url']
