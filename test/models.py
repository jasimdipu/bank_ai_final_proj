from django.db import models


# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'test'

    def __str__(self):
        return self.name


class TestModel2(models.Model):
    name = models.ForeignKey(TestModel, models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'test2'

    def __str__(self):
        return self.name.name
