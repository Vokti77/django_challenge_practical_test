from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CompanyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CompanyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CompanyUserManager()

    def __str__(self):
        return self.email


class Company(models.Model):
    user = models.OneToOneField(CompanyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desination = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name
 

class Device(models.Model):
    DEVICE_CHOICES = (
    ("Desktop", "Desktop"),
    ("Laptop", "Laptop"),
    ("IP Phone", "IP Phone"),
)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100, unique=True)
    derviceType = models.CharField(max_length=10, choices=DEVICE_CHOICES)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    options = (
        ('handed_out', 'Handed_Out'),
        ('returned', 'Returned'), 
    )
    status = models.CharField(max_length=50, choices=options, default='handed_out')
    checked_out_at = models.DateTimeField(null=True, blank=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.assigned_to.name} -{self.device.name} - {self.checked_out_at}"