from django.urls import path
from . import views
urlpatterns = [
    path('lists/',views.product,name='product_lists'),
]