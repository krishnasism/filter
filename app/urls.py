from django.urls import path
from . import views

urlpatterns=[
        path('',views.homePageView, name='home'),
        path('filter/',views.imageUpload,name='applyfilter'), 
      
        ]  