from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.fun,name='fun'),

    # path('add',views.addition,name='add'),

]