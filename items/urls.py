from django.urls import path

from items.views import ItemView, ItemListView

urlpatterns = [
    path('items/<int:id>/', ItemView.as_view(), name='items'),
    path('items/', ItemListView.as_view(), name='items'),
]
