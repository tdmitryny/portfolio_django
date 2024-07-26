from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostListDetailsView,ContactForm,ContactView, SuccessView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
    path('post/', views.PostListDetailsView.as_view(), name='post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
