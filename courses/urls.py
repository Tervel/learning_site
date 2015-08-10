from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list,),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail), # Above courses so that we don't accidently accept below
    url(r'(?P<pk>\d+)/$', views.course_detail), # Searches for /courses/n
]
