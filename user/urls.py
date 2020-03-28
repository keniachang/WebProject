from django.urls import path
from . import views
from .views import (
    PaymentEditView, ShippingEditView, 
    PaymentDeleteView, ShippingDeleteView
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/payment/', views.payment_list, name='payment_home'),
    path('profile/payment/edit/<int:pk>/', PaymentEditView.as_view() , name='payment_edit'),
    path('profile/payment/new', views.add_payment, name='add_payment'),
    path('profile/payment/delete/<int:pk>/', PaymentDeleteView.as_view() , name='payment_delete'),
    path('profile/shipping/', views.shipping_list, name='shipping_home'),
    path('profile/shipping/edit/<int:pk>/', ShippingEditView.as_view() , name='shipping_edit'),
    path('profile/shipping/new', views.add_shipping, name='add_shipping'),
    path('profile/shipping/delete/<int:pk>/', ShippingDeleteView.as_view() , name='shipping_delete'),

]

