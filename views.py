from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

from .models import *


# Create your views here.
class UserViewsets(viewsets.ModelViewSet):
    queryset = user.objects.all().values()
    serializer_class = UserSerializers

class DietitianViewsets(viewsets.ModelViewSet):
    queryset = dietitian.objects.all().values()
    serializer_class = DietitianSerializers


class PatientViewsets(viewsets.ModelViewSet):
    queryset = patient.objects.all().values()
    serializer_class = PatientSerializers


class AppointmentViewsets(viewsets.ModelViewSet):
    queryset = appointment.objects.all().values()
    serializer_class = AppointmentSerializers


class InvoiceViewsets(viewsets.ModelViewSet):
    queryset = invoice.objects.all().values()
    serializer_class = InvoiceSerializers


class AssistantViewsets(viewsets.ModelViewSet):
    queryset = assistant.objects.all().values()
    serializer_class = AssistantSerializers


class ProgramViewsets(viewsets.ModelViewSet):
    queryset = program.objects.all().values()
    serializer_class = ProgramSerializers


class Health_TipsViewsets(viewsets.ModelViewSet):
    queryset = health_tips.objects.all().values()
    serializer_class = Health_TipsSerializers


class Food_SystemViewsets(viewsets.ModelViewSet):
    queryset = food_system.objects.all().values()
    serializer_class = Food_SystemSerializers


class Meal_TypeViewsets(viewsets.ModelViewSet):
    queryset = meal_type.objects.all().values()
    serializer_class = Meal_TypeSerializers


class DetailsViewsets(viewsets.ModelViewSet):
    queryset = details.objects.all().values()
    serializer_class = DetailsSerializers


class Foodsystem_MealtypeViewsets(viewsets.ModelViewSet):
    queryset = foodsystem_mealtype.objects.all().values()
    serializer_class = Foodsystem_MealtypeSerializers


class ItemViewsets(viewsets.ModelViewSet):
    queryset = item.objects.all().values()
    serializer_class = ItemSerializers
