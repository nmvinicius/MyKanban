from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.newTarefa, name='newTarefa'),
    path('del/<int:pk>/', views.delTarefa, name='delTarefa'),
    path('upEstado/<int:pk>', views.upEstado, name='upEstado'),
]
