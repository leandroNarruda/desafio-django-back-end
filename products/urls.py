from django.urls import path
from .views import ProductView

urlpatterns = [
    path('products/<int:product_id>/', ProductView.as_view()),
]