from django.urls import path,URLPattern

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name= 'delete'),
    path('edit/<int:post_id>/', views.edit, name= 'edit'),
    path('like/<int:post_id>/',views.likes, name='like'),
    path('dislike/<int:post_id>/',views.dislikes, name='dislike')
]
