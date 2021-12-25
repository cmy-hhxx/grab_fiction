from django.urls import path
from . import views

app_name = 'grab_fiction'

urlpatterns = [
    path('', views.grab_novel, name='grab_novel'),
    path('novel_show/', views.novel_show, name='novel_show'),
]
