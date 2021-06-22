from rest_framework import serializers

from .models import Item, Review


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['articul', 'name', 'author', 'poster', 'author_img', 'description', 'price', 'action', 'previous_price', 'event_date']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'text', 'img']