from django.urls import path
from .import views

urlpatterns = [
    path('user/', views.studentList.as_view(), name='result')
]
