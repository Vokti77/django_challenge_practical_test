from django.urls import path
from assets.views import (
    ListUsers,
    CompanyRegistrationView,
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    DeviceLogListCreateView,
    DeviceLogRetrieveUpdateDestroyView,
)


urlpatterns = [
    path('', ListUsers.as_view(), name="list"),
    path('register/', CompanyRegistrationView.as_view(), name='company-registration'),
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(),
         name='employee-detail'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(),
         name='device-detail'),
    path('devicelogs/', DeviceLogListCreateView.as_view(), name='devicelog-list'),
    path('devicelogs/<int:pk>/', DeviceLogRetrieveUpdateDestroyView.as_view(),
         name='devicelog-detail'),
]