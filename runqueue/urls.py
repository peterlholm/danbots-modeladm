"RunQueue urls"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job', views.job , name='job'),
    #path('jobget', views.job_get , name='jobget'),
    path('jobstatus', views.job_status , name='jobstatus'),
    path('jobdelete', views.job_delete , name='jobdelete'),
    path('joblist', views.job_list , name='joblist'),
    path('jobnext', views.job_next , name='jobnext'),
]
