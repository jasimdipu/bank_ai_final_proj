from django.contrib import admin
from .models import TestModel, TestModel2


# Register your models here.
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


class TestModel2Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    list_filter = ('id',)


admin.site.register(TestModel, TestModelAdmin)
admin.site.register(TestModel2, TestModel2Admin)
