from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from couriers.models import Courier
from profiles.models import Customer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_orders': '/all',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/order/pk/delete',
        'Details': '/order/pk',
        'Courier orders': 'courier_my_orders/',
        'Customer orders': 'customer_my_orders/'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_orders(request):
    order = OrderSerializer(data=request.data)

    if Order.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if order.is_valid():
        order.save()
        return Response(order.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_orders(request):
    if request.query_params:
        orders = Order.objects.filter(**request.query_param.dict())
    else:
        orders = Order.objects.all()

    if orders:
        data = OrderSerializer(orders, many=True).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_orders(request, pk):
    order = Order.objects.get(pk=pk)
    data = OrderSerializer(instance=order, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_orders(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def order_details(request, pk):
    order = Order.objects.get(pk=pk)
    if order:
        data = OrderSerializer(order).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def courier_my_orders(request):
    user = request.user
    courier = Courier.objects.get(user=user)
    if courier:
        orders = Order.objects.filter(courier=courier)
    if orders:
        data = OrderSerializer(orders, many=True).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def customer_my_orders(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    if customer:
        orders = Order.objects.filter(customer=customer)
    if orders:
        data = OrderSerializer(orders, many=True).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        result = super(UserRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
        password=cd['password1'])
        login(self.request, user)
        return result

