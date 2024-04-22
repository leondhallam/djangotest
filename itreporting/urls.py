from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView

app_name = 'itreporting'
urlpatterns = [

    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('report', PostListView.as_view(), name = 'report'),
    path('issue/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)