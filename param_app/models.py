from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class UserGroup(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=100)
    class Meta:
        db_table = "p_userGroup"

class UserInfo(models.Model):
    user_level = (
        (1, "普通用户"),
        (2, "vip"),
        (3, "svip"),
    )

    userName = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    user_type = models.IntegerField(choices=user_level)
    group = models.ForeignKey("UserGroup", on_delete=models.CASCADE)
    role = models.ManyToManyField("Role")
    class Meta:
        db_table = "p_userInfo"

class UserToken(models.Model):
    user = models.OneToOneField("UserInfo", on_delete=models.CASCADE)
    token = models.CharField(max_length=100, default="")
    class Meta:
        db_table = "p_userToken"


class Role(models.Model):
    title = models.CharField(max_length=32)
    class Meta:
        db_table = "p_role"