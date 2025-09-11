from django.urls import path
from . import views
urlpatterns = [
    path('lists/',views.product,name='product_lists'),
    path('<int:product_id>/',views.productdetails, name='product_details'),
    path('cart/',views.cart_lists,name='cart_lists'),
    path('cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
]