from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view())
]
