# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# from django.db import models



# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

# class CarMake(models.Model):
#     name = models.CharField(max_length=100)  # Car make name
#     description = models.TextField()  # Description of the car make

#     def __str__(self):
#         return f"Car Make: {self.name}"  # String representation

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

# class CarModel(models.Model):
#     SEDAN = 'Sedan'
#     SUV = 'SUV'
#     WAGON = 'Wagon'
#     CAR_TYPES = [
#         (SEDAN, 'Sedan'),
#         (SUV, 'SUV'),
#         (WAGON, 'Wagon'),
#     ]

#     car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-one relationship
#     dealer_id = models.IntegerField()  # Refers to a dealer in Cloudant database
#     name = models.CharField(max_length=100)  # Car model name
#     type = models.CharField(max_length=10, choices=CAR_TYPES)  # Car type (limited choices)
#     year = models.DateField()  # Manufacturing year

#     def __str__(self):
#         return f"{self.car_make.name} - {self.name} ({self.type})"





# In your app's models.py

# from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type_choices = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
    ]
    type = models.CharField(max_length=20, choices=car_type_choices)
    year = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
