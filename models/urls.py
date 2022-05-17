"Trainmodels urls"
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainmodel', views.train_model , name='trainmodel'),
    path('trainlog', views.train_log , name='trainlog'),
    path('traindelete', views.train_delete , name='traindelete'),
    path('trainlist', views.train_list , name='trainlist'),
    path('simmodel', views.sim_model , name='simmodel'),
    path('simdelete', views.sim_delete , name='simdelete'),
    path('simlist', views.sim_list , name='simlist'),
]
