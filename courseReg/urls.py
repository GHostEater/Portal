from django.conf.urls import url
from courseReg import views

urlpatterns = [
    url(r'^course-to-major/', views.course_to_major, name='courseToMajor'),
]
