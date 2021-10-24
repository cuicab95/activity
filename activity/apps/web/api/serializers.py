from rest_framework import serializers
from ..models import *


class PropertyPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'title', 'address')


class ActivityPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'schedule', 'title', 'created_at_datetime', 'status')

    def to_representation(self, instance):
        representation = super(ActivityPreviewSerializer, self).to_representation(instance)
        representation['property'] = PropertyPreviewSerializer(instance=instance.property).data
        representation['survey'] = "https://test.com"
        return representation


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        exclude = ('created_at_datetime', 'updated_at_datetime', 'status')

    def to_representation(self, instance):
        representation = {'activities': ActivityPreviewSerializer(instance=instance).data}
        return representation

