from django.urls import path
from .import views
app_name = 'home'
urlpatterns = [
    path('', views.index , name='home'),
    path('product/', views.product , name='product'),
    path('product/<int:id>', views.productDetail , name='productDetail'),
    path('category/<int:id>', views.categoryDetail , name='categoryDetail'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('cart/', views.cart , name='cart'),
    path('loginpage/', views.loginpage , name='loginpage'),
    path('logout/', views.logoutpagee, name='logout'),
    path('register/', views.register, name='register'),

    path('checkout/', views.checkout , name='checkout'),
    path('search/', views.search , name='search'),

]