from rest_framework import viewsets
from rest_framework import generics
from books import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializers
    queryset = models.Books.objects.all()

class OrderBooksByDate(generics.ListAPIView):
    serializer_class = serializers.OrderBooksByDate
    def get_queryset(self):
        queryset = models.Books.objects.order_by('realease_year')
        return queryset

