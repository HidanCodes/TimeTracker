from rest_framework import serializers
from .models import User, Project, TimeEntry

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'id_device')
        read_only_fields = ('id',)

class DeviceAuthSerializer(serializers.Serializer):
    id_device = serializers.UUIDField()

class TimeEntrySerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    project = category = serializers.SlugRelatedField(
        queryset=Project.objects.all(),
        slug_field='title'
    )
    class Meta:
        model = TimeEntry
        fields = ('id', 'project', 'start_time',
                  'description', 'duration', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
    time_entries=TimeEntrySerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created_at', 'updated_at','time_entries')
        read_only_fields = ('created_at', 'updated_at')