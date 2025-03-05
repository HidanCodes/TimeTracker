from rest_framework import serializers
from .models import User, Project, TimeEntry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'id_device','first_name','last_name')
        read_only_fields = ('id',)

class DeviceAuthSerializer(serializers.Serializer):
    id_device = serializers.UUIDField()

class TimeEntrySerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.title', read_only=True)
    class Meta:
        model = TimeEntry
        fields = ('id', 'project', 'project_name', 'start_time',
                  'description', 'duration', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
    time_entries=TimeEntrySerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description','user', 'created_at', 'updated_at','time_entries')
        read_only_fields = ('created_at', 'updated_at')