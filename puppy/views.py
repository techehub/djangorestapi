
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PuppySerializer
from .models import Puppy


class PuppyDetail(APIView):

    def get_data(self, pk):
        try:
            puppy = Puppy.objects.get(pk=pk)
            return (puppy)  # This needed to be added.
        except Puppy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        puppy = self.get_data(pk)
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)

    def put(self, request, pk):
        puppy = self.get_data(pk)
        serializer = PuppySerializer(puppy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        puppy = self.get_data(pk)
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PuppyList(APIView):
    #get all
    def get(self, request):
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    # create
    def post(self, request):
        serializer = PuppySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)