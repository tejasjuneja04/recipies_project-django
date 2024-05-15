from django.urls import path

from . import views

app_name='recipies_list_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.admin1, name='upload'),
]