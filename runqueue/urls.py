"RunQueue urls"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job', views.job , name='job'),
    path('jobget', views.job_get , name='jobget'),
    path('jobdelete', views.job_delete , name='jobdelete'),
    path('joblist', views.job_list , name='joblist'),
]
