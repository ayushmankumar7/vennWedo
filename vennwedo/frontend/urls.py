from django.urls import path 
from . import views 

urlpatterns = [ 
	path('', views.index),
	path('login', views.index),
	path('live', views.index)
]