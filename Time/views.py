
from.models import User,Project,TimeEntry
from Time.Serializers import UserSerializer,ProjectSerializer,TimeEntrySerializer

from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework.views import APIView # type:ignore


class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TimeEntiryView(APIView)    :
    def get(self, request):
        time = TimeEntry.objects.all()
        serializer = TimeEntrySerializer(time, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = TimeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView) :
    def get (self,request,pk):
        try:
            user=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put (self,request,pk):
        try:
            user=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            Post=User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Post.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)

class ProjectsDetail(APIView) :
    def get (self,request,pk):
        try:
            projects=Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projects)
        return Response(serializer.data)

    def put (self,request,pk):
        try:
            projects=Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(projects,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            projects=Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        projects.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)


class TimeEntiryDetail(APIView) :
    def get (self,request,pk):
        try:
            times=TimeEntry.objects.get(pk=pk)
        except TimeEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TimeEntrySerializer(times)
        return Response(serializer.data)

    def put (self,request,pk):
        try:
            times=TimeEntry.objects.get(pk=pk)
        except TimeEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TimeEntrySerializer(times,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            times=TimeEntry.objects.get(pk=pk)
        except TimeEntry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        times.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)