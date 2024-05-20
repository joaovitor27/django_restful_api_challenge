from rest_framework import serializers

from items.serializers import ItemSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'created_at']


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['items']
        read_only_fields = ['user', 'created_at']
