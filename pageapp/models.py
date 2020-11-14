from django.db import models

# Create your models here.

class Silk(models.Model):
    name = models.CharField(max_length=50,unique=True)
    price = models.CharField(max_length=10)

    class Meta:
        db_table = 'tb_silk'


class Company(models.Model):
    com_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "tb_company"

class Phone(models.Model):
    phone_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    class Meta:
        db_table = "tb_phone"


if __name__ == '__main__':


    pass





