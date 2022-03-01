"Trainmodels urls"
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainmodel', views.trainmodel , name='train'),
    path('deletemodel', views.delete_model , name='delete'),
    path('list', views.list_models , name='list'),
]
