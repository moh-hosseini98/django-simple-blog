from django.urls import path

from . import views



app_name = 'accounts'

urlpatterns = [

    path('register/',views.register,name='register'),
    path('logout/',views.logoutuser,name='logout'),
    path('login/',views.loginpage,name='login'),

]