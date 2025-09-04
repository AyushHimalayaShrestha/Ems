from django.shortcuts import render, redirect
from product.forms import CategoryForm, ProductForm
from product.models import Product,Category
from django.contrib import messages
from users.auth import admin_only
from django.contrib.auth.decorators import login_required
# Create your views here.


# Category
@admin_only
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_category_lists')
    else:
        form=CategoryForm()
        
    return render(request,'add_category.html',{'form':form})

# Category List
def category_list(request):
    category_lists = Category.objects.all()
    return render(request,'dashboard_category_lists.html',{'category_lists':category_lists})

# Update Category
@admin_only
@login_required
def update_category(request, category_id):
    instance = Category.objects.get(id=category_id)
    if request.method =="POST":
        form =CategoryForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('dashboard_category_lists')
        else:
            messages.error(request, 'Error Updating.')
    else:
        form =CategoryForm(instance=instance)
        return render(request,'updatecategory.html',{'form':form})
    
# Delete Category
@admin_only
@login_required
def delete_category(request, category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.success(request,"Category deleted successfully")
    return redirect('dashboard_category_lists')



# Product
@admin_only
@login_required
def add_product(request):
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_product_lists')
    else:
        form = ProductForm()
    return render(request,'add_product.html',{'form':form})

# Product List
def product_list(request):
    product_lists = Product.objects.all()
    return render(request,'dashboard_product_lists.html',{'product_lists':product_lists})

# Update Product
@admin_only
@login_required
def update_product(request, product_id):
    instance = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form= ProductForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('dashboard_product_lists')
        else:
            messages.error(request, 'Error Updating.')
    else:
        form= ProductForm(instance=instance)
        return render(request,'updateproduct.html',{'form':form})
    
# Delete Product
@admin_only
@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('dashboard_product_lists')