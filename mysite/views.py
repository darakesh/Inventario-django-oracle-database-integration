from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST

from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 

from .models import product
from .forms import productform

# Create your views here.


def home_view(request):
    all_products = product.objects.order_by("id")
   
    paginator = Paginator(all_products,5,1)
    pageNo = request.GET.get('page',1)
    try:
        products = paginator.get_page(pageNo)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    form = productform()
    context = {'products' : products, 'productform' : form, "productCount" : all_products.count() }

    return render(request,'inventory.html',context)

@require_POST
def add_product(request):
    form = productform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Product Created sucessfully!")
    else:
        for err in form.errors:
            messages.error(request,form.errors[err][0])
    return redirect('home')

@require_POST
def edit_product(request,pk):
    item = product.objects.get(id = pk)
    form = productform( request.POST, instance= item)
    if form.is_valid():
        form.save()
        messages.success(request, "Product Edited sucessfully!")
    else:
        for err in form.errors:
            messages.error(request,form.errors[err][0])
    return redirect('home')

@require_POST
def delete_product(request,pk):
    item = product.objects.get(id = pk)
    item.delete()
    messages.success(request, "Product Deleted sucessfully!")
    return redirect("home")
