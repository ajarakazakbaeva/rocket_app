from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_orders': '/all',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/order/pk/delete'
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