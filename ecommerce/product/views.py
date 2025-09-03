from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

# View for displaying product lists
def product(request):
    product_list=Product.objects.all().order_by("-id")
    context={
        'products': product_list
    }
    return render(request,'product/product_lists.html',context)

def productdetails(request,product_id):
    product= Product.objects.get(id = product_id)
    data ={
        'product':product
    }
    return render(request,'product/productdetails.html', data)


# cart lists
@login_required
def cart_lists(request):
    return render(request, "cart/cart.html")