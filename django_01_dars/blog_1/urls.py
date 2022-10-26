from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name="first"),
    path('bahor/', views.bahor, name="bahor"),
    path('yoz/', views.yoz, name="yoz"),
    path('kuz/', views.kuz, name="kuz"),
    path('qish/', views.qish, name="qish"),
]
