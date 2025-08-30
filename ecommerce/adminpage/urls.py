from django.urls import path
from . import views
urlpatterns=[
    path('category/add',views.add_category,name='add_category'),
    path('product/add',views.add_product,name='add_product'),
    path('product/lists',views.product_list,name='dashboard_product_lists'),
    path('category/lists',views.category_list,name='dashboard_category_lists'),
    path('product/<int:product_id>/',views.update_product,name='update_product'),
    path('product/delete/<int:product_id>/',views.delete_product,name='delete_product'),

]