from django.shortcuts import render, redirect
from product.forms import CategoryForm, ProductForm
from django.contrib import messages
# Create your views here.


# Category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form=CategoryForm()
        
    return render(request,'add_category.html',{'form':form})

# Product
def add_product(request):
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request,'add_product.html',{'form':form})

# Update Product
def update_product(request, product_id):
    instance = ProductForm.objects.get(id=product_id)
    if request.method == 'POST':
        form= ProductForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('product_lists')
        else:
            messages.error(request, 'Error Updating.')
    else:
        form= ProductForm(instance=instance)