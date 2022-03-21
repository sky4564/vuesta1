
from django.urls import path, include

from .views import FeedList

urlpatterns = [
    path('feed/', FeedList.as_view()),
]