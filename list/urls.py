from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies,name = 'movies' ),
    path('add/', views.add,name = 'add' ),
    path('delete/<int:id>', views.delete,name = 'delete' ),
    path('update/<int:id>', views.update,name = 'update' ),
    path('details/<int:id>/', views.detail, name = 'detail')
]
