from rest_framework import serializers
from .models import User, Project, TimeEntry

class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # لیست آی‌دی‌های پروژه‌های کاربر
    # project_titles = serializers.CharField(source='projects.title', read_only=True)
    # projects = serializers.SlugRelatedField(
    #     queryset=Project.objects.all(),  # اینجا مدل یوزر را استفاده کن
    #     slug_field='title'  # نمایش نام کاربری به‌جای id
    # )

    class Meta:
        model = User
        fields = ('id','device_id','projects', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),  # اینجا مدل یوزر را استفاده کن
        slug_field='device_id'  # نمایش نام کاربری به‌جای id
    )
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'user', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class TimeEntrySerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = TimeEntry
        fields = ('id', 'project', 'start_time', 'description', 'duration', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def get_duration(self, obj):  # متد get_duration باید دقیقا همین‌طور باشد
        # اینجا می‌توانید منطق سفارشی خود را برای مدت زمان وارد کنید
        return str(obj.duration)  # به عنوان مثال تبدیل duration به رشته
