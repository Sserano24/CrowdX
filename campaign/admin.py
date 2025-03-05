from django.contrib import admin
from .models import Category, Customer, Project, Order
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Order)