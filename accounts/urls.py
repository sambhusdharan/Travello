from django.urls import path,include
from . import views

urlpatterns=[

    path('register',views.register,name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('news/', views.News, name='news'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
]