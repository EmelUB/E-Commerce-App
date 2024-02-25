from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    search=""
    if request.GET.get('query'):
        search = request.GET.get('query') 
        products = Product.objects.filter(name__icontains=search)
        
    context = {
        'products':products,
        'search':search
    }

    return render(request,'index.html',context)


def detail(request,productId):
    product = Product.objects.get(id = productId)
    context = {
        'product':product
    }
    return render(request,'detail.html',context)


def create(request):
    form = ProductForm() #formu boş şekilde gösterecek.
    if request.method =='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            newProduct = form.save(commit=False) # önce ürün oluşturup sonra owner bilgisi eklemek için bunu yaptık.2 kere db ye  kaydetmemesi için commit False yaptık.
            newProduct.owner = request.user  #hangi oturum açıksa onu owner yapcak.
            newProduct.save()
            messages.success(request,'Ürününüz Oluşturuldu.')
            return redirect('index')
        else: print(form.errors)
    context ={
        'form':form
        }
    return render(request,'create.html',context)


