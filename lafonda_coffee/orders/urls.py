from django.urls import path
from .views import MyOrderDetailView

urlpatterns = [
    path('my-orders/', MyOrderDetailView.as_view(), name='my_order'),
]
