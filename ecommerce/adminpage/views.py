from django.shortcuts import render, redirect
from product.forms import CategoryForm
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm()
        if form.is_valid():
            form.save()
            redirect('add_category')
    else:
        form=CategoryForm()
        context ={
            'form':form
        }
    return render(request,'add_category.html')