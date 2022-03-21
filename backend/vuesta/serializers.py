from rest_framework import serializers

from .models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            "name",
            "userImage",
            "postImage",
            "likes",
            "date",
            "liked",
            "content",
            "filter",
        )