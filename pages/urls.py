from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductListView, ProductCreatedView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='product-index'),
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('products/<str:id>/', ProductShowView.as_view(), name='show'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product-created/', ProductCreatedView.as_view(), name='product-created'),
]