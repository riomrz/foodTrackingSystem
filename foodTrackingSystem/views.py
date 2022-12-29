import json
from django.shortcuts import get_object_or_404, render
from foodTrackingSystem.forms import ProductForm

from foodTrackingSystem.models import Product

def insert_code(request):
    if request.method == "GET":
        print('SONO NELLA GET')
        form = ProductForm()
        return render(request, 'foodTrackingSystem/insert_code.html', {'form': form})
    elif request.method == "POST":
        print('SONO NELLA POST')
        print('request.POST: ', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            print('form is valid')
            code = request.POST.get('code')
            print('code: ', code)
            product = Product.objects.filter(code=code).get() # sempre singolo product
            print('product: ', product)
        return render(request, 'foodTrackingSystem/product_detail.html', {'form': form, 'product': product})
        


def product_detail(request, code):
    product = get_object_or_404(Product, code=code)
    return render(request, 'foodTrackingSystem/product_detail.html')
