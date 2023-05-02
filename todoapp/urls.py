from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page-index'),
    path('todoapp/', views.homepage, name='homepage')
]
