from django.contrib import admin
from .models import *


# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'phonenumber', 'address', 'gender']


class dietatianAdmin(admin.ModelAdmin):
    list_display = ['experience_years', 'clinic_address']

class patientAdmin(admin.ModelAdmin):
    list_display = ['blood_type', 'age', 'height', 'thyroid', 'pressure_disease', 'heart_disease', 'soft_drink',
                    'work_type', 'vegetarian']


class assistantAdmin(admin.ModelAdmin):
    list_display = ['work_hours', 'experience_years']


class appointmentAdmin(admin.ModelAdmin):
    list_display = ['weight', 'date', 'medical_test',]


class invoiceAdmin(admin.ModelAdmin):
    list_display = ['date_invoice', 'value']


class programAdmin(admin.ModelAdmin):
    list_display = ['program_code', 'description']


class health_tipsAdmin(admin.ModelAdmin):
    list_display = ['sport_tips', 'food_tips', 'life_style_tips']


class food_systemAdmin(admin.ModelAdmin):
    list_display = ['program_type']


class foodsystem_mealtypeAdmin(admin.ModelAdmin):
    list_display = ['fs', 'mt', 'dtls']


class meal_typeAdmin(admin.ModelAdmin):
    list_display = ['name', 'meal_time']


class detailsAdmin(admin.ModelAdmin):
    list_display = ['description', 'quantity']


class itemAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'calories']


admin.site.register(user, userAdmin)
admin.site.register(dietitian, dietatianAdmin)
admin.site.register(patient, patientAdmin)
admin.site.register(assistant, assistantAdmin)
admin.site.register(appointment, appointmentAdmin)
admin.site.register(invoice, invoiceAdmin)
admin.site.register(program, programAdmin)
admin.site.register(health_tips, health_tipsAdmin)
admin.site.register(food_system, food_systemAdmin)
admin.site.register(foodsystem_mealtype, foodsystem_mealtypeAdmin)
admin.site.register(details, detailsAdmin)
admin.site.register(item, itemAdmin)

