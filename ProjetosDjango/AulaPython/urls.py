from django.contrib import admin
from django.urls import path
from app1.views import index_int,index_str, index_hora



urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:valor>', index_int),
    path('<str:valor>', index_str),
    path('saudacao/<str:nome>/', index_hora)
]
