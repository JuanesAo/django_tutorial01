from django.urls import path
from django.conf import settings
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductListView, ProductCreatedView, ProductTableView, CartView, CartAddView, CartRemoveAllView, ImageViewFactory
from .utils import ImageLocalStorage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='product-index'),
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('products/<str:id>/', ProductShowView.as_view(), name='show'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product-table/', ProductTableView.as_view(), name='product-table'),
    path('product-created/', ProductCreatedView.as_view(), name='product-created'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/removeAll/', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
]