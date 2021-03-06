"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from pages.views import home_view
from book.views import book_detail_view
from cart.views import cart_view
from comment.views import comment_view
from wishlist.views import wishlist_view
from book.views import bookdetail_view
from book.views import authorbook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('books/', book_detail_view, name='books'),
    path('cart/', cart_view, name='cart'),
    path('', include('user.urls'), name='register'),
    path('', include('user.urls'), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('comment/', comment_view, name='comment'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('books/bookdetail/', bookdetail_view, name='bookdetail'),
    path('books/bookdetail/authorbook/<str:author>', authorbook_view, name='authorbook')
]
