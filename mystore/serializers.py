from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Order, Product
from couriers.models import Courier
from profiles.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id', 'user', 'address', 'phone_number'
        )
        read_only_fields = ('user', 'address', 'phone_number')


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = (
            'id', 'user', 'address', 'phone_number'
        )
        read_only_fields = ('user', 'address', 'phone_number')

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = (
#             'id'
#         )

class OrderSerializer(serializers.ModelSerializer):
    # customer = PrimaryKeyRelatedField(read_only=True)
    # courier = serializers.IntegerField()
    # customer = serializers.SlugRelatedField(queryset=Customer.objects.all(), slug_field='customer')
    # courier = serializers.SlugRelatedField(queryset=Courier.objects.all(), slug_field='courier')
    customer = CustomerSerializer(read_only=True)
    courier = CourierSerializer(read_only=True)
    destination = serializers.CharField()
    # created_at = serializers.DateTimeField()
    requested_delivery_date = serializers.DateTimeField()
    weight = serializers.IntegerField()
    status = serializers.CharField(max_length=255)
    # order_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # order_item = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='product')
    # order_item = ProductSerializer(read_only=True, many=True)
    def to_representation(self, instance):
        self.fields['customer'] = CustomerSerializer(read_only=True)
        self.fields['courier'] = CourierSerializer(read_only=True)
        return super(OrderSerializer, self).to_representation(instance)

    class Meta:
        model = Order
        # fields = ('customer', 'courier', 'destination', 'requested_delivery_date', 'weight', 'status')
        fields = ('customer', 'courier', 'destination', 'requested_delivery_date', 'weight', 'status')
        # fields = ('destination', 'weight', 'status')
        # fields = ("__all__")