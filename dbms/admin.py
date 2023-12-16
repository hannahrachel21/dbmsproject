from django.contrib import admin
from dbms.models import members
from dbms.models import employee
from dbms.models import adminlogin
# Register your models here.
admin.site.register(members)
admin.site.register(employee)
admin.site.register(adminlogin)