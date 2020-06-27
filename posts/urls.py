from django.urls import path

from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('search/',views.search,name='search'),
    path('blog/<str:id>/',views.post,name='detail'),
   
    
    
]