from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['articul', 'name', 'author', 'poster', 'author_ing', 'description', 'price', 'action', 'previous_price', 'event_date']