from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('sign-up',views.sign_up,name='sign-up'),
    path('create/task',views.addTask,name='addTask'),
    path('update/<int:pk>',views.updateTask, name='update'),
    # path('/about',views.about,name='about')
]