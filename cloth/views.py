from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'cloth/product_list.html', {'products': products})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'cloth/category_list.html', {'categories': categories})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'cloth/product_detail.html', {'product': product})


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'cloth/category_detail.html', {'category': category})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm()
    return render(request, 'cloth/product_form.html', {'form': form})


def product_edit(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None, instance = product)
        if form.is_valid():
            product = form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance = product)
    return render(request, 'cloth/product_form.html', {'form': form})


def product_delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect('product_list')
