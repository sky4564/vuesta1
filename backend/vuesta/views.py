from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Feed
from .serializers import FeedSerializer


class FeedList(APIView):
    def get(self, request, format=None):
        feed = Feed.objects.all()
        serializer = FeedSerializer(feed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
