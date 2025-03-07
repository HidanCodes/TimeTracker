from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Time.views import UserView, ProjectView, TimeEntiryView, UserDetail, ProjectsDetail, TimeEntiryDetail, \
    DeviceAuthView,Welcome

schema_view = get_schema_view(
    openapi.Info(
        title="My APIs",
        default_version='v1',
        description="Api for app",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('auth/device/', DeviceAuthView.as_view(), name='device-auth'),
    path('userview/',UserView.as_view()),
    path('projectview/',ProjectView.as_view()),
    path('TimeEntiryView/',TimeEntiryView.as_view()),
    path('userdetailview/',UserDetail.as_view()),
    path('projectview/<int:pk>/',ProjectsDetail.as_view()),
    path('TimeEntiryView/<int:pk>/',TimeEntiryDetail.as_view()),
    path('welcome/',Welcome.as_view()),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]