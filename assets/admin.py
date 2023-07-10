from django.contrib import admin
from assets.models import CompanyUser, Company, Employee, Device, DeviceLog

admin.site.register(Company)
admin.site.register(CompanyUser)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)
