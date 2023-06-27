from django.contrib.auth.models import User, Group
from .models import Book
from rest_framework import viewsets
from .serializers import UserSerializer,GroupSerializer,Seriali
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView


@api_view(['POST'])
def update(request, pk):
    item = Book.objects.get(pk=pk)
    data = Seriali(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
@api_view(['POST'])
def post(request):
    query = Seriali(data=request.data)
    if query.is_valid():
        query.save()
        return Response(query.data)
    

class User(viewsets.ViewSet):
      def list(self,request):
          queryset = User.objects.all()
          serializer = UserSerializer(queryset, many=True)
          return Response(serializer.data)

      def retrieve(self, request, id=None):
          print(request)
          queryset = User.objects.get(id=id)
          print(queryset)
          serializer = UserSerializer(queryset)
          return Response(serializer.data)

class Group(viewsets.ViewSet):
      def list(self,request):
          queryset = Group.objects.all()
          serializer = GroupSerializer(queryset, many=True)
          return Response(serializer.data)

      def retrieve(self, request, id=None):
          print(request)
          queryset = Group.objects.get(id=id)
          print(queryset)
          serializer = GroupSerializer(queryset)
          return Response(serializer.data)

class Serial(viewsets.ViewSet):
      def list(self,request):
          queryset = Book.objects.all()
          serializer = Seriali(queryset, many=True)
          return Response(serializer.data)

      def retrieve(self, request, id=None):
          print(request)
          queryset = Book.objects.get(id=id)
          print(queryset)
          serializer = Seriali(queryset)
          return Response(serializer.data)

