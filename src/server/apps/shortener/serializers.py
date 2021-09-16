from rest_framework import serializers
from models import URL


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['address', 'label', 'slug', 'visits', 'created']
        read_only_fields = ['slug', 'visits', 'created']
