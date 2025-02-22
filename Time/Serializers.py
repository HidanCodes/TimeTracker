from rest_framework import serializers
from .models import User, Project, TimeEntry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'device_id', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'user', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class TimeEntrySerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = TimeEntry
        fields = ('id', 'project', 'start_time',
                  'description', 'duration', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')