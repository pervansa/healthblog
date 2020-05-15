from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [

    #API to post a comment
    # path('comment/', views.commenthome, name='commenthome'),
    path('', views.postComment, name='postComment')
    
]