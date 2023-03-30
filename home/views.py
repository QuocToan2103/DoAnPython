from django.http import HttpResponse
from category.models import Category

from product.models import Product

from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.shortcuts import render , redirect
from home.forms import CustomUserForm

# Create your views here.
def index(request):
    pro = Product.objects.all()
    cate = Category.objects.all()
    context={
       'pro':pro,
       'cate':cate
    }
    return render(request , 'page/home.html', context )

def product(request):
    pro = Product.objects.all()
    cate = Category.objects.all()
    context={
       'pro':pro,
       'cate':cate
    }
    return render(request , 'page/product.html', context )

def about(request): 
    return render(request , 'page/about.html')

def contact(request): 
    return render(request , 'page/contact.html')

def checkout(request): 
    return render(request , 'page/checkout.html')

def productDetail(request, id): 
    proDetail = Product.objects.get(id = id) 
    return render(request, 'page/productDetail.html', {'proDetail': proDetail})

def categoryDetail(request, id): 
    cateDetail = Category.objects.get(id = id) 
    return render(request, 'page/categoryDetail.html', {'cateDetail': cateDetail})

def cart(request): 
    return render(request , 'page/cart.html')


# def login(request): 
#     return render(request , 'page/login.html')

# def register(request): 
#     return render(request , 'page/register.html')


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            pro = Product.objects.filter(name__contains=query)
           
            return render(request , 'page/search.html', {'pro': pro})
        else:
            print("No information to show")
            return request(request, 'page/search.html', {})

def register(request):
    form = CustomUserForm()
    if request.method =='POST':
         form = CustomUserForm(request.POST)
         if form.is_valid():
              form.save()
              messages.success(request, "Registered Successfully! Login to Continue")
              return redirect('/loginpage')
    context = {'form': form}
    return render(request , 'page/register.html', context)

def loginpage(request):
    if  request.user.is_authenticated:
         messages.warning(request, "You are already logged in")
         return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username') 
            passwd = request.POST.get('password') 

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login (request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invalid Username or Passwrod")
                return redirect('/loginpage')      
        return render(request, "page/login.html")
    


def logoutpagee(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect('/')

# cart = {}      
# def addcart(request):
#     if request.is_ajax():
#         id = request.POST.get('id')
#         num = request.POST.get('num')

#         proDetail = Product.objects.get(id = id)
#         if id in cart.keys():
#             itemCart = {
#                 'name' : proDetail.name,
#                 'price' : proDetail.price,
#                 'image' : str(proDetail.image),
#                 'num' : int (cart[id]['num']) + 1
#             }
#         else :
#             itemCart = {
#                 'name' : proDetail.name,
#                 'price' : proDetail.price,
#                 'image' : str(proDetail.image),
#                 'num' : num
#             }
#         cart[id] = itemCart
#         request.session['cart'] = cart
#         cartInfo = request.session['cart']
#     return render(request , 'page/addcart.html', {'pro': pro})


# def _cart_id(request):
#     cart_id = request.session.session_key
#     if not cart_id:
#         cart_id = request.session.create()
#     return cart_id

# def add_cart(request, product_id):
#     current_user = request.user
#     product = Product.objects.get(id=product_id)    # Get object product
#     if current_user.is_authenticated:
#         product_variations = list()
#         if request.method == 'POST':
#             for item in request.POST:
#                 key = item
#                 value = request.POST.get(key)
#                 try:
#                     variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
#                     product_variations.append(variation)
#                 except ObjectDoesNotExist:
#                     pass

#         is_exists_cart_item = CartItem.objects.filter(product=product, user=current_user).exists()
#         if is_exists_cart_item:
#             cart_items = CartItem.objects.filter(
#                 product=product,
#                 user=current_user
#             )
#             existing_variation_list = [list(item.variations.all()) for item in cart_items]
#             id = [item.id for item in cart_items]
#             if product_variations in existing_variation_list:
#                 idex = existing_variation_list.index(product_variations)
#                 cart_item = CartItem.objects.get(id=id[idex])
#                 cart_item.quantity += 1
#             else:
#                 cart_item = CartItem.objects.create(
#                     product=product,
#                     user=current_user,
#                     quantity=1
#                 )
#         else:
#             cart_item = CartItem.objects.create(
#                 product=product,
#                 user=current_user,
#                 quantity=1
#             )
#         if len(product_variations) > 0:
#             cart_item.variations.clear()
#             for item in product_variations:
#                 cart_item.variations.add(item)
#         cart_item.save()
#         return redirect('cart')
#     else:
#         product_variations = list()
#         if request.method == 'POST':
#             for item in request.POST:
#                 key = item
#                 value = request.POST.get(key)
#                 try:
#                     variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
#                     product_variations.append(variation)
#                 except ObjectDoesNotExist:
#                     pass
#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request=request))  # Get cart using the _cart_id
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(
#                 cart_id=_cart_id(request)
#             )
#         cart.save()

#         is_exists_cart_item = CartItem.objects.filter(product=product, cart=cart).exists()
#         if is_exists_cart_item:
#             cart_items = CartItem.objects.filter(
#                 product=product,
#                 cart=cart
#             )
#             existing_variation_list = [list(item.variations.all()) for item in cart_items]
#             id = [item.id for item in cart_items]
#             if product_variations in existing_variation_list:
#                 idex = existing_variation_list.index(product_variations)
#                 cart_item = CartItem.objects.get(id=id[idex])
#                 cart_item.quantity += 1
#             else:
#                 cart_item = CartItem.objects.create(
#                     product=product,
#                     cart=cart,
#                     quantity=1
#                 )
#         else:
#             cart_item = CartItem.objects.create(
#                 product=product,
#                 cart=cart,
#                 quantity=1
#             )
#         if len(product_variations) > 0:
#             cart_item.variations.clear()
#             for item in product_variations:
#                 cart_item.variations.add(item)
#         cart_item.save()
#         return redirect('cart')


# def remove_cart(request, product_id, cart_item_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         if request.user.is_authenticated:
#             cart_item = CartItem.objects.get(
#                 id=cart_item_id,
#                 product=product,
#                 user=request.user
#             )
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_item = CartItem.objects.get(
#                 id=cart_item_id,
#                 product=product,
#                 cart=cart
#             )
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#     except Exception:
#         pass
#     return redirect('cart')


# def remove_cart_item(request, product_id, cart_item_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         if request.user.is_authenticated:
#             cart_item = CartItem.objects.get(
#                 id=cart_item_id,
#                 product=product,
#                 user=request.user
#             )
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request=request))
#             cart_item = CartItem.objects.get(
#                 id=cart_item_id,
#                 product=product,
#                 cart=cart
#             )
#         cart_item.delete()
#     except Exception:
#         pass
#     return redirect('cart')


# def cart(request, total=0, quantity=0, cart_items=None):
#     try:
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.filter(user=request.user, is_active=True)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request=request))
#             cart_items = CartItem.objects.filter(cart=cart, is_active=True)
#         for cart_item in cart_items:
#             total += cart_item.product.price * cart_item.quantity
#             quantity += cart_item.quantity
#         tax = total * 2 / 100
#         grand_total = total + tax
#     except ObjectDoesNotExist:
#         pass    # Chỉ bỏ qua
#     print(request.user)
#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax': tax if "tax" in locals() else "",
#         'grand_total': grand_total if "tax" in locals() else 0,
#     }
#     return render(request, 'store/cart.html', context=context)

# @login_required(login_url='login')
# def checkout(request, total=0, quantity=0, cart_items=None):
#     try:
#         # cart = Cart.objects.get(cart_id=_cart_id(request=request))
#         cart_items = CartItem.objects.filter(user=request.user, is_active=True)
#         for cart_item in cart_items:
#             total += cart_item.product.price * cart_item.quantity
#             quantity += cart_item.quantity
#         tax = total * 2 / 100
#         grand_total = total + tax
#     except ObjectDoesNotExist:
#         pass    # Chỉ bỏ qua
#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax': tax if "tax" in locals() else "",
#         'grand_total': grand_total,
#     }
#     return render(request, 'store/checkout.html', context=context)