from rest_framework import serializers
from .models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genres']
