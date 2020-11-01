from django.db import models

# Create your models here.

SEX = (
    (1, "man"),
    (2, "woman")
)


class Persons(models.Model):

    name = models.CharField(max_length=100, verbose_name="姓名", help_text="姓名")
    # sex = models.IntegerField(verbose_name="性别", help_text="性别", default="1", choices=SEX)
    phone = models.CharField(max_length=11, verbose_name="手机号", help_text="手机号")
    address = models.CharField(max_length=200, verbose_name="家庭住址", help_text="家庭住址", blank=True, null=True)

    class Meta:
        db_table = "tb_person"



