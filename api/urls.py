"Trainmodels urls"
from django.urls import path

from . import views

urlpatterns = [
    path('save', views.save_training, name='save'),
    path('savetrain', views.save_training, name='savetrain'),
    path('savesim', views.save_sim, name='savesim'),]
