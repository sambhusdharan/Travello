from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='fun'),
    path('destination/',views.destination,name='destination'),
    # path('add',views.addition,name='add'),

]