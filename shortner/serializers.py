from rest_framework import serializers
from .models import UrlDetailes
import random
import string


class UrlDetailesSerailizer(serializers.Serializer):
    original_url = serializers.CharField(max_length=1000)
    # shorted_url = serializers.CharField(max_length=15)

    def create(self, validated_data):
        validated_data['shorted_url'] = shortit(validated_data['original_url'])
        try:
            ins = UrlDetailes.objects.get(
                original_url=validated_data['original_url'])
            ins.delete()
            return UrlDetailes.objects.create(**validated_data)
        except:
            return UrlDetailes.objects.create(**validated_data)


def shortit(original_url):
    # shortner length
    N = 7
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # generate a random string of length 7
    surl = ''.join(random.choices(s, k=N))
    return surl
