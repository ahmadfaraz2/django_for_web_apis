from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "subtitle", "author", "isbn"]


# A "serilizer" translate complex data like [queryset] and [model instances]
# into a format that is easy to consume over the internet, typically "JSON".
