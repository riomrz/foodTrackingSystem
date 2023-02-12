from django.shortcuts import get_object_or_404, render
from foodTrackingSystem.forms import *
from django.core.exceptions import EmptyResultSet
from django.contrib.auth import authenticate, login
from foodTrackingSystem.models import Product

def insert_code(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'foodTrackingSystem/insert_code.html', {'form': form})
    elif request.method == "POST":
        form = ProductForm()
        code = request.POST.get('code')
        if code:
            product = Product()
            products = Product.objects.filter(code=code) # only one product is returned
            if products:
                product = products.get()
                return render(request, 'foodTrackingSystem/product_detail.html', {'form': form, 'product': product})
            return render(request, 'foodTrackingSystem/product_detail.html', {'form': form})
        return render(request, 'foodTrackingSystem/insert_code.html', {'form': form})

def product_detail(request, code):
    product = get_object_or_404(Product, code=code)
    return render(request, 'foodTrackingSystem/product_detail.html')