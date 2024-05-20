from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
