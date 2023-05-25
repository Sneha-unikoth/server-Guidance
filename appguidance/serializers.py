from rest_framework import serializers
from disabled.models import Log,userreg,shopreg,workshop,product,order,payment,feedback,notification,complaints,counciling,shop



class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields ='__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = userreg
        fields = '__all__'
        def create(self,validated_data):
            return userreg.objects,create(**validated_data)

class ShopRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = shopreg
        fields = '__all__'
        def create(self,validated_data):
            return shopreg.objects,create(**validated_data)  

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = workshop
        fields = '__all__'
        def create(self,validated_data):
            return workshop.objects,create(**validated_data)           

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
        def create(self,validated_data):
            return product.objects,create(**validated_data)           

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
        def create(self,validated_data):
            return order.objects,create(**validated_data)      

class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
        def create(self,validated_data):
            return payment.objects,create(**validated_data)           

class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'
        def create(self,validated_data):
            return feedback.objects,create(**validated_data)           

class notificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = '__all__'
        def create(self,validated_data):
            return notification.objects,create(**validated_data)           


class complaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = complaints
        fields = '__all__'
        def create(self,validated_data):
            return complaints.objects,create(**validated_data)           


class councilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = counciling
        fields = '__all__'
        def create(self,validated_data):
            return counciling.objects,create(**validated_data)           



class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'
        def create(self,validated_data):
            return shop.objects,create(**validated_data) 