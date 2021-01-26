from rest_framework import serializers
from books import models

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'

class OrderBooksByDate(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'
    