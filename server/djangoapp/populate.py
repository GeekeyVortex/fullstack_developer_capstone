# # def initiate():
# #     print("Populate not implemented. Add data manually")


# from .models import CarMake, CarModel

# def initiate():
#     car_make_data = [
#         {"name":"NISSAN", "description":"Great cars. Japanese technology"},
#         {"name":"Mercedes", "description":"Great cars. German technology"},
#         {"name":"Audi", "description":"Great cars. German technology"},
#         {"name":"Kia", "description":"Great cars. Korean technology"},
#         {"name":"Toyota", "description":"Great cars. Japanese technology"},
#     ]

#     car_make_instances = []
#     for data in car_make_data:
#             car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


#     # Create CarModel instances with the corresponding CarMake instances
#     car_model_data = [
#       {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
#       {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
#       {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
#       {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
#       {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
#       {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
#       {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
#       {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
#       {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
#       {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
#       {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
#       {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3]},
#       {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
#       {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
#       {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
#         # Add more CarModel instances as needed
#     ]

#     for data in car_model_data:
#             CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])





# redefined populate.py

# import sys
# import os
# import django

# # Set the correct path to the settings module
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# # Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')

# # Initialize Django
# django.setup()

# from djangoapp.models import CarMake, CarModel

# def initiate():
#     car_make_data = [
#         {"name":"NISSAN", "description":"Great cars. Japanese technology"},
#         {"name":"Mercedes", "description":"Great cars. German technology"},
#         {"name":"Audi", "description":"Great cars. German technology"},
#         {"name":"Kia", "description":"Great cars. Korean technology"},
#         {"name":"Toyota", "description":"Great cars. Japanese technology"},
#     ]

#     car_make_instances = []
#     for data in car_make_data:
#         car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

#     # Create CarModel instances with the corresponding CarMake instances
#     car_model_data = [
#       {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make": car_make_instances[0]},
#       {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make": car_make_instances[0]},
#       {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make": car_make_instances[0]},
#       {"name":"A-Class", "type":"SUV", "year": 2023, "car_make": car_make_instances[1]},
#       {"name":"C-Class", "type":"SUV", "year": 2023, "car_make": car_make_instances[1]},
#       {"name":"E-Class", "type":"SUV", "year": 2023, "car_make": car_make_instances[1]},
#       {"name":"A4", "type":"SUV", "year": 2023, "car_make": car_make_instances[2]},
#       {"name":"A5", "type":"SUV", "year": 2023, "car_make": car_make_instances[2]},
#       {"name":"A6", "type":"SUV", "year": 2023, "car_make": car_make_instances[2]},
#       {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make": car_make_instances[3]},
#       {"name":"Carnival", "type":"SUV", "year": 2023, "car_make": car_make_instances[3]},
#       {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make": car_make_instances[3]},
#       {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make": car_make_instances[4]},
#       {"name":"Camry", "type":"Sedan", "year": 2023, "car_make": car_make_instances[4]},
#       {"name":"Kluger", "type":"SUV", "year": 2023, "car_make": car_make_instances[4]},
#     ]

#     for data in car_model_data:
#         CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])

# if __name__ == "__main__":
#     initiate()



import sys
import os
import django

# Set the correct path to the settings module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')  # Replace 'djangoproj' with your project name

# Initialize Django
django.setup()

from djangoapp.models import CarMake, CarModel  # Replace 'djangoapp' with your app name

def initiate():
    # CarMake data
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    # Create CarMake instances
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    # CarModel data with corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},
    ]

    # Create CarModel instances
    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])

if __name__ == "__main__":
    initiate()
