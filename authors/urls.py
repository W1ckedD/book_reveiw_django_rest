from django.urls import path
from .views import AuthorBookAPIView, AuthorsAPIView, AuthorAPIView

urlpatterns = [
  path('', AuthorsAPIView.as_view()),
  path('<int:id>', AuthorAPIView.as_view()),
  path('<int:id>/books', AuthorBookAPIView.as_view()),
]