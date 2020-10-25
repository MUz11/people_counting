from .models import counting
from rest_framework import serializers
#
#
class countSerializer(serializers.ModelSerializer):
     class Meta:
         model = counting
         fields = [
             'id',
             'location',
                   'time',
                   'human_in',
                   'human_out']