from django.views.generic import DetailView
from django.shortcuts import render
from .models import Order

# Create your views here.
class MyOrderDetailView(DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'orders'

    def get_object(self, queryset = None):
        return Order.objects.filter(is_active = True, user = self.request.user).all()
    
    


