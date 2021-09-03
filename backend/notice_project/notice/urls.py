from django.urls import path
from .views import CreateNoticeView, CommentReactionAPIView, AllNoticesView

#add url routes here

urlpatterns = [

    path('notices/', CreateNoticeView.as_view()),

    path('all-notices', AllNoticesView.as_view()),

    path('comment/reaction/update', CommentReactionAPIView.as_view()),
    
]
