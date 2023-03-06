from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class meta:
        model = user
        fields = ['fullname', 'email', 'phonenumber', 'address', 'gender']

class DietitianSerializers(serializers.ModelSerializer):
    class meta:
        model = dietitian
        fields = ['experience_years', 'clinic_address']


class PatientSerializers(serializers.ModelSerializer):
    class meta:
        model = patient
        fields = ['blood_type', 'age', 'height', 'thyroid', 'pressure_disease', 'heart_disease', 'soft_drink',
                  'work_type', 'vegetarian']


class AppointmentSerializers(serializers.ModelSerializer):
    class meta:
        model = appointment
        fields = ['weight', 'date', 'medical_test']


class InvoiceSerializers(serializers.ModelSerializer):
    class meta:
        model = invoice
        fields = ['date_invoice', 'value']


class AssistantSerializers(serializers.ModelSerializer):
    class meta:
        model = assistant
        fields = ['work_hours', 'experience_years']


class ProgramSerializers(serializers.ModelSerializer):
    class meta:
        model = program
        fields = ['program_code', 'description']


class Health_TipsSerializers(serializers.ModelSerializer):
    class meta:
        model = health_tips
        fields = ['sport_tips', 'food_tips', 'life_style_tips']


class Food_SystemSerializers(serializers.ModelSerializer):
    class meta:
        model = food_system
        fields = ['program_type']


class Meal_TypeSerializers(serializers.ModelSerializer):
    class meta:
        model = meal_type
        fields = ['name', 'meal_time']


class DetailsSerializers(serializers.ModelSerializer):
    class meta:
        model = details
        fields = ['description', 'quantity']


class Foodsystem_MealtypeSerializers(serializers.ModelSerializer):
    class meta:
        model = foodsystem_mealtype
        fields = ['fs', 'mt', 'dtls']


class ItemSerializers(serializers.ModelSerializer):
    class meta:
        model = item
        fields = ['name', 'unit', 'calories']