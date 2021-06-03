from django.shortcuts import render , redirect
from .models import product
from .forms import productform
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
# Create your views here.

def pagination(request, location = None):
    all_products = product.objects.order_by("id")
    paginator = Paginator(all_products,5,2)
    if location == "END":
        pageNo = paginator.num_pages
    else:
        pageNo = request.GET.get('page',1)
    try:
        products = paginator.get_page(pageNo)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return products,all_products.count()

def home_view(request):
    
    if request.POST.get("btn") == "Add":
        form = productform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Added sucessfully!!!")
            products, count = pagination(request ,"END")
    else:
         products, count = pagination(request)        
    form = productform()
    btn = "Add"
    context = {'products': products , 'productform' : form , 'btnval' : btn , "productCount" : count }

    return render(request,'main.html',context)
    
def edit_view(request,pk):
    item = product.objects.filter(id = pk)
    form = productform(instance=item.first())
    btn = "Save"
    products, count = pagination(request)
    print(request)
    print(request.GET)
    print(products)
   
    if request.POST.get("btn") == "Save":
        form = productform( request.POST, instance= item.first())
        if form.is_valid():
            form.save()
            messages.success(request, "Product Edited sucessfully!!!")
            products, count = pagination(request, "CURRENT")
    
    context = {'products':products , 'productform' : form , 'btnval' : btn , "productCount" : count }

    return render(request,'main.html',context)


def delete_view(request,pk):
    item = product.objects.get(id = pk)
    item.delete()
    messages.success(request, "Product Deleted sucessfully!!!")
    return redirect("home")



def home_view(request):
    all_products = product.objects.order_by("id")
    paginator = Paginator(all_products,5,2)
    pageNo = request.GET.get('page',1)
    try:
        products = paginator.get_page(pageNo)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    form = productform()
    btn = "Add"
    context = {'products':products , 'productform' : form , 'btnval' : btn , "productCount" : all_products.count() }
    return render(request,'main.html',context)

def add_product(request):
    pass

def edit_product(request):
    pass

def delete_product(request):
    pass
