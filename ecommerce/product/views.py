from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
@login_required()
def cart_lists(request):
    user_cart = Cart.objects.filter(user=request.user)
    # Calculate total price for each cart item
    for item in user_cart:
       item.total=item.product.product_price * item.quantity

    # Calculate overall total price
    overall_total = sum(item.total for item in user_cart)

    return render(request, "cart/cart.html", {'cart_items': user_cart, 'overall_total': overall_total})

# add to cart
@login_required()
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity_str= request.POST.get('quantity','1')
    quantity=int(quantity_str) if quantity_str and quantity_str.isdigit() and int(quantity_str) > 0 else 1
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': quantity}
        )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
        messages.success(request, f"{product.product_name} added to cart successfully")
   
    return redirect('cart_lists')
    
