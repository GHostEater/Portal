from django.conf.urls import url
from voting import views

urlpatterns = [
    url(r'^voter/new/$', views.voter_create),
    url(r'^voter/$', views.VoterAPIView.as_view()),
    url(r'^voter/(?P<user>[0-9]+)/$', views.VoterDetailAPIView.as_view()),

    url(r'^post/$', views.PostAPIView.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailAPIView.as_view()),

    url(r'^candidate/$', views.CandidateAPIView.as_view()),
    url(r'^candidate/(?P<pk>[0-9]+)/$', views.CandidateDetailAPIView.as_view()),

    url(r'^vote/new/$', views.VoteCreateAPIView.as_view()),
    url(r'^vote/$', views.VoteAPIView.as_view()),
    url(r'^vote/(?P<pk>[0-9]+)/$', views.VoteDetailAPIView.as_view()),

    url(r'^vote-result/new/$', views.ResultCreateAPIView.as_view()),
    url(r'^vote-result/$', views.ResultAPIView.as_view()),
    url(r'^vote-result/(?P<pk>[0-9]+)/$', views.ResultDetailAPIView.as_view()),

    url(r'^voting-status/(?P<pk>[0-9]+)/$', views.VotingStatusAPIView.as_view()),
]
