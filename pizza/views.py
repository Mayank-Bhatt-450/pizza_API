from django.shortcuts import render

# Create your views here.
from . import models
from .models import pizza_model
from .serializers import pizza_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class pizza_view(APIView):

    def get(self, request):
        pizza = models.pizza_model.objects.all()
        serializer = pizza_serializer(pizza, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = pizza_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class pizza_api_(APIView):

    def get_object(self, id):
        try:
            return models.pizza_model.objects.get(id=id)
        except:
            return 'not found'


    def get(self, request, id):
        pizza = self.get_object(id)
        print(pizza)
        if pizza=='not found':
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = pizza_serializer(pizza)
            #print(serializer.data)
            return Response(serializer.data)

    def put(self, request,id):
        models.pizza_model = self.get_object(id)
        if pizza=='not found':
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = pizza_serializer(models.pizza_model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            a=serializer.errors
            a['Valid_pizza_type_options']='regular , squar'
            a['Valid_pizza_size_options']='small, medium, large'
            return Response(a, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pizza = self.get_object(id)
        if pizza=='not found':
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            pizza_model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
class pizza_search(APIView):

    def get(self, request,obj):

        pizza =list(models.pizza_model.objects.filter(pizza_size=obj))+list(models.pizza_model.objects.filter(pizza_type=obj))

        serializer = pizza_serializer(pizza, many=True)
        return Response(serializer.data)
