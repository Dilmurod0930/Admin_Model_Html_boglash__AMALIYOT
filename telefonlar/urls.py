from  django.urls import  path
from .views import  home ,  telefon_list, telefon_info

urlpatterns = [
    path('', home,  name='home'),
    path('telefon_list', telefon_list, name='telefon_list'),
    path('telefon<int:pk>/', telefon_info, name='telefon_info'),
]