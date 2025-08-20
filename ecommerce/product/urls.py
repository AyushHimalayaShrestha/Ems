from django.urls import path
from . import views
urlpatterns = [
    path('lists/',views.product,name='product_lists'),
    path('<int:product_id>/',views.productdetails, name='product_details')
]