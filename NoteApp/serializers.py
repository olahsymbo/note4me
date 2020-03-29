from .models import Notes, Category
from rest_framework import serializers
#serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'content', 'created', 'due_date', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')