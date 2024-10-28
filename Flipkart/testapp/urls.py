from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup_page'),
    path('',views.index_page,name='index_page'),
    path('items/',views.cart_items_list,name='cart_items'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout/',views.logout_view,name='logout_page'),
    path('buynowitem/<int:id>/',views.buy_now,name='buynow'),
    path('itemdelete/<int:id>/',views.CartItemDelete,name='CartItemDelete'),
    path('items/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('buy_now/<int:id>/',views.buy_now_from_cart,name='buy_now')
]