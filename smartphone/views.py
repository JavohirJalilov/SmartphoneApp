import json
from math import prod
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
# Create your views here.
def home(request):
    context = {
        'all_products':'http://djangoadmin.pythonanywhere.com/products',
        'by_company':'https://djangoadmin.pythonanywhere.com/products/company/Apple',
        'by_RAM':'https://djangoadmin.pythonanywhere.com/products/ram/4',
        'by_memory':'https://djangoadmin.pythonanywhere.com/products/memory/32'
    }
    return render(request, 'index.html', context=context)
def convert_to_json(product):
    """
    Convert a product to a JSON object
    args:
        product: a product object
    returns:
        a JSON object
    """
    product_json = {
        'id': product.id,
        'name': product.name,
        'company': product.company,
        'color': product.color,
        'RAM': product.RAM,
        'memory': product.memory,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'img_url': product.img_url,
    }
    return product_json
    
def add_product(request):
    """
    Create a product
    args:
        request: the request object
    return:
        JsonResponse: the product
    """
    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST['name'],
            company=request.POST['company'],
            color=request.POST['color'],
            RAM=request.POST['RAM'],
            memory=request.POST['memory'],
            price=request.POST['price'],
            img_url=request.POST['img_url'],
        )
        product_json = convert_to_json(product)
        product.save() # save the product to the database
        
        return JsonResponse({'product': product_json})

    return JsonResponse({'product': {}})

def get_products(request):
    """
    Get all products
    args:
        request: the request object
    return:
        JsonResponse: the list of products
    """
    products = Product.objects.all()
    products_json = []
    for product in products:
        products_json.append(convert_to_json(product))


    return JsonResponse({'products': products_json})


def delete_product(request, id):
    """
    Delete a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        product.delete()
    return JsonResponse({'product': {}})

def get_products_by_company(request, company):
    """
    Get all products by company
    args:
        request: the request object
        company: the company of the product
    return:
        JsonResponse: the list of products
    """
    products_json = []
    if request.method == 'GET':
        products = Product.objects.filter(name__contains=company)
        for product in products:
            products_json.append(convert_to_json(product))
    return JsonResponse({"products":products_json})

def get_products_by_RAM(request, RAM):
    """
    Get all products by company
    args:
        request: the request object
        company: the company of the product
    return:
        JsonResponse: the list of products
    """
    products_json = []
    if request.method == 'GET':
        products = Product.objects.filter(RAM__contains=RAM)
        for product in products:
            products_json.append(convert_to_json(product))
    
    return JsonResponse({'products':products_json})

def get_products_by_memory(request, memory):
    """
    Get all products by company
    args:
        request: the request object
        company: the company of the product
    return:
        JsonResponse: the list of products
    """
    products_json = []
    if request.method == 'GET':
        products = Product.objects.filter(memory__contains=memory)
        for product in products:
            products_json.append(convert_to_json(product))
    
    return JsonResponse({'products':products_json})

