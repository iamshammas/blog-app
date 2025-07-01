from django.urls import path,include
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('loginn',views.loginn,name='loginn'),
    path('',views.index,name='index'),
    path('posts',views.posts,name='posts'),
    path('mypost',views.mypost,name='mypost'),
    path('createpost',views.createpost,name='createpost'),
    path('logout_view',views.logout_view,name='logout_view'),
]
