from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Feed
from .serializers import FeedSerializer


class FeedList(APIView):
    def get(self, request, format=None):
        feed = Feed.objects.all()
        serializer = FeedSerializer(feed, many=True)
        return Response(serializer.data)
