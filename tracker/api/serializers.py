from rest_framework import serializers
from ..models import Habit, HabitLog
from django.contrib.auth.models import User

class HabitSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.CharField(source='get_absolute_url', read_only=True)
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Habit
        fields = ['url', 'id', 'name', 'description', 'user']

class HabitLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HabitLog
        fields = ['url', 'id', 'habit', 'date', 'completed']