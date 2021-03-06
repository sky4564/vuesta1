from django.http import Http404
from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import APIView
from rest_framework.response import Response

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

class FeedDetail(APIView):
    def get_object(self, pk):
        try:
            return Feed.objects.get(pk=pk)
        except Feed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        feed = self.get_object(pk)
        context = request.data
        serializer = FeedSerializer(feed, data=context, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        feed = self.get_object(pk)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeFeed(APIView):
    def get_object(self, pk):
        try:
            return Feed.objects.get(pk=pk)
        except Feed.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):

        feed = self.get_object(pk)
        
        if feed.liked:
            serializer = FeedSerializer(feed, data={'liked': False, 'likes': feed.likes-1}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            serializer = FeedSerializer(feed, data={'liked': True, 'likes': feed.likes+1}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

