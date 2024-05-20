from django.urls import path

from orders.views import OrderCreateView, UserOrdersView, OrderDetailView

urlpatterns = [
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/user/', UserOrdersView.as_view(), name='user-orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
