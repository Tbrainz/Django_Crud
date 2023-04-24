from django.db import models

# Create your models here.
class Marital(models.Model):
    status = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.status

class Profile(models.Model):
    fullname = models.CharField(max_length=200)
    mobile = models.IntegerField()
    age = models.IntegerField()
    status = models.ForeignKey(Marital, on_delete=models.CASCADE)


    def __str__(self):
        return self.fullname