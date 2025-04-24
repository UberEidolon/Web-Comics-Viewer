from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
     path('manga/<int:manga_id>/page-<int:page_number>/', views.manga_detail, name='manga_detail'),
]
