from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.permissions import BasePermission
from .models import Company, CompanyUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from assets.models import  Employee, Device, DeviceLog
from .serializers import UserSerializer, UserSerializer
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer


class CompanyRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        reg_serializer = UserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser: 
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        company_id = view.kwargs.get('company_id')
        if company_id and request.user.is_authenticated:
            return request.user.employee.company_id == int(company_id)
        return False


class ListUsers(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
      
        usernames = [user.name for user in Company.objects.all()]
        return Response(usernames)

class CompanyListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceLogListCreateView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [IsAuthenticated]


class DeviceLogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [IsAuthenticated]