from django.contrib import admin
from .models import CustomerData


# Register your models here.
class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'experience', 'income', 'education']
    search_fields = ['zip_code']
    list_filter = ['age', 'experience']


admin.site.register(CustomerData, CustomerDataAdmin)
