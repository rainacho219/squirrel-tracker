from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('add/', views.AddSighting.as_view(), name='add'),
        path('stats/', views.stats, name='stats'),
        path('<pk>/', views.update, name='update'),
        path('<pk>/delete/', views.delete, name='delete'),
]
