from django.conf.urls import url
from coursereview import views

urlpatterns = [
    url(r'^course-review/$', views.CourseReviewAPIView.as_view()),
    url(r'^course-review/new/$', views.CourseReviewCreateAPIView.as_view()),
    url(r'^course-review/student/$', views.CourseReviewStudentAPIView.as_view()),
    url(r'^course-review/lecturer/$', views.CourseReviewLecturerAPIView.as_view()),
    url(r'^course-review/course/$', views.CourseReviewCourseAPIView.as_view()),
    url(r'^course-review/(?P<pk>[0-9]+)/$', views.CourseReviewDetailAPIView.as_view()),
]
