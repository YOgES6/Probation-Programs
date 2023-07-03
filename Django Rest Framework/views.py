from django.contrib.auth.models import User, Group
from .models import Book
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializers import UserSerializer,Seriali,RegisterSerializer,UpdateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect


@api_view(['POST'])
def update(request, pk):
    item = Book.objects.get(pk=pk)
    data = Seriali(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)

@api_view(['POST'])
def userupdate(request, pk):
    item = User.objects.get(pk=pk)
    data = UserSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)

@api_view(['POST'])
def post(request):
    query = Seriali(data=request.data)
    if query.is_valid():
        query.save()
        return Response(query.data)
 
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

class Register(generics.GenericAPIView):
      serializer_class = RegisterSerializer

      def post(self, request, *args, **kwargs):
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          user = serializer.save()
          return Response({
          "user": UserSerializer(user, context=self.get_serializer_context()).data,})
      
class UserList(generics.ListCreateAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer

      def list(self, request):
          queryset = self.get_queryset()
          serializer = UserSerializer(queryset, many=True)
          return Response(serializer.data)
      
      def update(self, request, *args, **kwargs):
          serializer = self.serializer_class(data=request.data, partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)
      
class List(APIView):
      renderer_classes = [TemplateHTMLRenderer]
      template_name = 'my.html'
      def get(self, request):
          queryset = Book.objects.all()
          return Response({'data': queryset})

class UpdateUser(generics.CreateAPIView):
      queryset = User.objects.all()
      serializer_class = UpdateSerializer
      permission_classes = (permissions.IsAuthenticated,)

