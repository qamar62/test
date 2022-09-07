from django.urls import path
from .views import BlogView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('', BlogView.as_view(), name='all_blogs'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post', BlogCreateView.as_view(), name='add_post'),
    path('detail/edit/<int:pk>', BlogUpdateView.as_view(), name='update_post'),
    path('detail/<int:pk>/remove', BlogDeleteView.as_view(), name='delete_post'),
]