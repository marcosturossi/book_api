from django.urls import path
from .views import ApiRoot, BookListCreateView, BookRetrieveUpdateDestroyView, CategoryListCreateView, \
    CategoryRetrieveUpdateDestroyView, CollectionRetrieveView, Documentation

app_name = 'collections'

urlpatterns = [
    path('documentation', Documentation.as_view(), name='documentation'),
    path('', ApiRoot.as_view(), name='api_root'),
    path('book-list', BookListCreateView.as_view(), name='book_list'),
    path('book-detail/<int:pk>', BookRetrieveUpdateDestroyView.as_view(), name='book_detail'),
    path('category-list', CategoryListCreateView.as_view(), name='category_list'),
    path('category-detail/<int:pk>', CategoryRetrieveUpdateDestroyView.as_view(), name='category_detail'),
    path('collection-detail/<int:pk>', CollectionRetrieveView.as_view(), name='collection_detail'),
]