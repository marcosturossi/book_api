from django.urls import path
from .views import BookAPIView

app_name = 'collections'

urlpatterns = [
    path('book-list', BookAPIView.as_view(), name='book-list')
]