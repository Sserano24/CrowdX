from django.db import models
import datetime

# Category model (e.g., charity, business, etc.)
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Customer model (users who fund projects)
class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

# Project model
class Project(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=2000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='project_images/')
    date = models.DateField(default=datetime.date.today) # Add date in the project
    def __str__(self):
        return self.name

# Order model (Transactions)
class Order(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    fund = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50, default='', blank=True, null=True)
    date = models.DateField(default=datetime.date.today)  # Corrected default value
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.project.name} by {self.customer.full_name}"
