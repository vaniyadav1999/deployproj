from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm,LoginForm
from .models import Cart,Product,CartItem
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    form = SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            Cart.objects.get_or_create(user=user)
            return HttpResponse("<h1>Success</h1>")
    return render(request,'signup.html',{"form":form})


def login_page(request):
    form = LoginForm()
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index_page')
            else:
                messages.error(request,'Invalid Credintial')
    return render(request,'login.html',{"form":form})


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login_page')
def index_page(request):
    products = Product.objects.all()    
    if request.method=='POST':
        product = request.POST.get('product')
        products = Product.objects.filter(name__icontains=product)
    username = Cart.objects.get(user=request.user)
    cart_products = CartItem.objects.filter(cart=username)
    return render(request,'index.html',{"products":products,'length':len(cart_products)})


def cart_items_list(request):
    username = Cart.objects.get(user=request.user)
    products = CartItem.objects.filter(cart=username)
    if len(products)==0:
        messages.error(request,'There is No Item in Your Cart')
    return render(request, 'cartitems.html', {"products": products})

def buy_now(request,id):
    cart = Product.objects.get(id=id)
    return render(request,'buyitem2.html',{"cart":cart})


def CartItemDelete(request,id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('cart_items')



def add_to_cart(request,id):
    product = get_object_or_404(Product, id=id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product,quantity=quantity)
        cart_item.save()
        messages.success(request, 'Item added to the cart')
        return redirect('index_page')
    return render(request, 'cart.html', {'product': product})


def buy_now_from_cart(request,id):
    cart= CartItem.objects.get(id=id)
    return render(request,'buyitem.html',{"cart":cart})