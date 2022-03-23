from rest_framework import serializers

from .models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            "id",
            "name",
            "userImage",
            "postImage",
            "get_userImage",
            "get_postImage",
            "likes",
            "date",
            "liked",
            "content",
            "filter",
        )