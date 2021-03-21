from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from mixins_views.models import Student
from mixins_views.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView #useing for class based views !

from rest_framework import generics,mixins




class StudentListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer


   def get(self,request):
      return self.list(request)

   def post(self,request):
      return self.create(request)




#primary key  based operation
class StudentDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer



   def get(self,request,pk):
      return self.retrieve(request,pk)


   def put(self,request,pk):
      return self.update(request,pk)


   def delete(self,request,pk):
      return self.destroy(request,pk)


