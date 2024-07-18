from django.urls import path, include
from . import views
# from .views import Post



urlpatterns = [
    path('', views.home, name='home'),
    # path('', Post.as_view(), name='home'),
    path('post/', views.post, name='post'),
    path('tinymce/', include('tinymce.urls')),
]
