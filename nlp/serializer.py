from rest_framework import serializers
from .models import testTask, Movie

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = testTask
        #fields = ('id', 'title', 'description', 'don')
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'