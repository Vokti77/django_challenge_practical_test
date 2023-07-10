from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CompanyUser, Company, Device, Employee, DeviceLog

class UserSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True)
    class Meta:
        model = CompanyUser
        fields = ['email', 'password', 'company_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        user = CompanyUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        Company.objects.create(user=user, name=company_name)
        return user
    

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'