from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        "nama_aplikasi": "Sutashop",
        "nama": "Vissuta Gunawan Lim",
        "kelas": "D",
        'products': products
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    products = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", products), content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    return HttpResponse(serializers.serialize("json", products), content_type="application/json")

def show_xml_by_id(request, pk):
    product = Product.objects.filter(id=pk)
    return HttpResponse(serializers.serialize("xml", product), content_type="application/xml")

def show_json_by_id(request,pk):
    product = Product.objects.filter(id=pk)
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")