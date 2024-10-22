from rest_framework import serializers
from .models import Book

from rest_framework.exceptions import ValidationError
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """It converts the Book model data to JSON and vice versa."""
    class Meta:
        model = Book
        fields = '__all__'

    def validate_published_date(self, value):
        """Ensure that the published date is not in the future."""
        if value > date.today():
            raise ValidationError("Published date cannot be in the future.")
        return value

    def validate_isbn_number(self, value):
        """ Ensure that the ISBN has exactly 13 characters."""
        if len(value) > 13:
            raise ValidationError("ISBN number must be 13 characters long.")
        return value