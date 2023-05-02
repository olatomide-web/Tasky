from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks_homepage, name='tasks-homepage'),
    path('<int:id>/',views.tasks_details, name='tasks_details'),
    path('delete/<int:id>/', views.tasks_delete, name='tasks_delete'),
    path('update/<int:id>/', views.tasks_update, name='tasks_update'),
    path('create/', views.tasks_create, name='tasks_create'),
    path('search/', views.tasks_search, name='tasks_search'),


]