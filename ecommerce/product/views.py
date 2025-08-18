from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# View for displaying product lists
def product(request):
    product_list=Product.objects.all()
    context={
        'products': product_list
    }
    return render(request,'product/product_lists.html',context)