from django.db import models
# from django.db.models.base import Model


# Create your models here.
class living(models.Model):
    pass

class Studyroom(models.Model):
    ProductID=models.IntegerField(default=True)
    Title=models.CharField(max_length=500,default=True)
    AMT=models.FloatField(default=True)
    Discount=models.IntegerField(null=True)
    IMG=models.CharField(max_length=2500,default=True)

    def __str__(self):
        return self.Title


