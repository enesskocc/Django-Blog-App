from django.urls import path
from .views import post_list, post_create, post_delete, post_update, post_details, post_like

urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('delete/<int:pk>', post_delete, name='delete'),
    path('update/<int:pk>', post_update, name='update'),
    path('detail/<int:pk>', post_details, name='detail'),
    path('post_like/<int:id>', post_like, name='like'),
]