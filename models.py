from django.db import models

blood_type = (
    ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-"))
thyroid = (("Yes", "Yes"), ("No", "No"))
pressure_disease = (("Yes", "Yes"), ("No", "No"))
heart_disease = (("Yes", "Yes"), ("No", "No"))
soft_drinks = (("Yes", "Yes"), ("No", "No"))
vegeterian = (("Yes", "Yes"), ("No", "No"))
gender = (("Female", "Female"), ("Male", "Male"))
work_type = (("Easy/does not need much effort", "Easy/does not need much effort"), ("Moderate", "Moderate"),
             ("Hard/needs big effort", "Hard/needs big effort"))
diabetes = (("yes", "yes"), ("No","No"))


# Create your models here.
class user(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    fullname = models.CharField(max_length=30, verbose_name="Enter your full name:")
    email = models.CharField(max_length=40, verbose_name="Your email address:")
    phonenumber = models.IntegerField(verbose_name="Phone number:")
    address = models.CharField(max_length=40, verbose_name="Your address:")
    gender = models.CharField(max_length=30, verbose_name="Select gender:", choices=gender, default="Female")


class dietitian(user):
    class Meta:
        verbose_name = "dietitian"
        verbose_name_plural = "dietitians"

    experience_years = models.IntegerField(verbose_name="Doctor's years experience:")
    clinic_address = models.CharField(max_length=40, verbose_name="Clinic address:")


class patient(user):
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"

    blood_type = models.CharField(verbose_name='Blood Type', max_length=10, choices=blood_type)
    age = models.IntegerField(verbose_name="Enter your age:")
    height = models.IntegerField(verbose_name="Enter your height:")
    thyroid = models.CharField(max_length=10, verbose_name="Do you have Thyroid problems?", choices=thyroid,
                               default="No")
    pressure_disease = models.CharField(max_length=10, verbose_name="Do you have Pressure?", choices=pressure_disease,
                                        default="No")
    heart_disease = models.CharField(max_length=10, verbose_name="Do you have Heart problems", choices=heart_disease,
                                     default="No")
    soft_drink = models.CharField(max_length=10, verbose_name="Do you drink soft-drinks a lot?", choices=soft_drinks,
                                  default="No")
    work_type = models.CharField(max_length=50, verbose_name="How is your work?", choices=work_type)
    vegetarian = models.CharField(max_length=10, verbose_name="Are you Vegeterian?", choices=vegeterian, default="No")
    diabetes = models.CharField(max_length=10 , verbose_name= "do you have diabetes?" , choices=diabetes , default="No")

class appointment(models.Model):
    class Meta:
        verbose_name = "appointment"
        verbose_name_plural = "appointments"
    weight = models.IntegerField(verbose_name="Patient weight:")
    date = models.DateField(verbose_name="Appointment date:", auto_now=True)
    medical_test = models.TextField(max_length=10, verbose_name="Patient medical examinations:")


class invoice(models.Model):
    date_invoice = models.DateField(verbose_name="Invoice date:", auto_now=True)
    value = models.FloatField(verbose_name="Cost")


class assistant(user):
    work_hours = models.IntegerField(verbose_name="Assistant worked hours:")
    experience_years = models.IntegerField(verbose_name="Assistant experience years:")


class program(models.Model):
    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"

    program_code = models.IntegerField(verbose_name="Program code:")
    description = models.TextField(max_length=100, verbose_name="Program description:")


class health_tips(models.Model):
    sport_tips = models.TextField(max_length=100, verbose_name="Sport tips:")
    food_tips = models.TextField(max_length=100, verbose_name="Food tips:")
    life_style_tips = models.TextField(max_length=100, verbose_name="Life style tips:")


class food_system(models.Model):
    program_type = models.CharField(max_length=30, verbose_name="Program type:")


class meal_type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Quantity:")
    meal_time = models.DateField(max_length=30, verbose_name="Quantity:")


class details(models.Model):
    description = models.TextField(max_length=100, verbose_name="Quantity:")
    quantity = models.IntegerField(verbose_name="Quantity:")


class foodsystem_mealtype(models.Model):
    fs = models.ForeignKey(food_system, on_delete=models.CASCADE, verbose_name="Food system:")
    mt = models.ForeignKey(meal_type, on_delete=models.CASCADE, verbose_name="Meal type:")
    dtls = models.ForeignKey(details, on_delete=models.CASCADE, verbose_name="Details:")


class item(models.Model):
    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"

    name = models.CharField(max_length=30, verbose_name="Item name:")
    unit = models.CharField(max_length=10, verbose_name="Unit used:")
    calories = models.FloatField(verbose_name="Portion calories:")

