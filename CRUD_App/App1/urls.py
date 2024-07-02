from django.urls import path
from. import views

urlpatterns = [
    path('home/',views.Home,name='Home'),
    path('',views.ShowFormData,name='My_Form'),
    path('Edit/<int:Roll_NO>/',views.Update,name='Update'),
    path('delete/<int:Roll_NO>/',views.Delete,name='Delete'),
]