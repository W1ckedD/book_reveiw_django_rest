from django.urls import path
from . import views

urlpatterns = [
  path('', views.BookList.as_view(), name='books'),
  path('<int:id>/', views.RetrieveBook.as_view(), name='book'),
  path('genre/<int:genre_id>/', views.BooksByGenre.as_view(), name='books_by_genre'),
]