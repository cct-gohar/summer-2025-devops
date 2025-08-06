from rest_framework import serializers
from .models import Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Field-level validation
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters long.")
        if not value.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits.")
        return value

    # Object-level validation
    def validate(self, data):
        published_date = data.get("published_date")
        if published_date and published_date > date.today():
            raise serializers.ValidationError(
                {"published_date": "Published date cannot be in the future."}
            )
        return data
