from . import views
from django.urls import path

urlpatterns = [
     path('recipes/', views.PostList.as_view(), name="recipes"),
     path('', views.home, name='home'),
     path('delete/', views.delete_comment, name='delete_comment'),
     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]