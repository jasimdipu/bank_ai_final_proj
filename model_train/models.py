from django.db import models


class CustomerData(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    experience = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    zip_code = models.CharField(max_length=10)
    family = models.IntegerField()
    ccavg = models.DecimalField(max_digits=5, decimal_places=2)
    education = models.IntegerField()
    mortgage = models.DecimalField(max_digits=10, decimal_places=2)
    personal_loan = models.BooleanField()
    securities_account = models.BooleanField()
    cd_account = models.BooleanField()
    online = models.BooleanField()
    creditcard = models.BooleanField()

    class Meta:
        db_table = 'customer_data'  # Replace with your actual table name
