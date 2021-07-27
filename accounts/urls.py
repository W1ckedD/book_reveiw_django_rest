from django.urls import path
from knox import views as knox_views
from . import views


urlpatterns = [
  path('register/', views.RegisterAPIView.as_view(), name='register'),
  path('login/', views.LoginAPIView.as_view(), name='register'),
  path('get-user/', views.RetrieveUserAPIView.as_view(), name='get-user'),
  path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')
]