
from django.urls import path, include

from .views import *

urlpatterns = [
    path('feed/', FeedList.as_view()),
    path('feed/detail/<int:pk>/', FeedDetail.as_view()),

]