from django.db import models

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name="项目名称", help_text="项目名称", unique=True)
    leader = models.CharField(max_length=50, verbose_name="负责人", help_text="负责人")
    tester = models.CharField(max_length=50, verbose_name="测试人员", help_text="测试人员")
    developer = models.CharField(max_length=50, verbose_name="开发人员", help_text="开发人员")
    publish_app = models.CharField(max_length=100, verbose_name="发布应用", help_text="发布应用")
    # null 设置该字段允许为空， blank用于设置前端可以不传递
    desc = models.TextField( verbose_name="简要描述", help_text="简要描述", blank=True, default="", null=True)

    # 用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_projects'
        # 会在admin站点中，显示一个更人性化的表明
        verbose_name = "项目"
        verbose_name_plural = "项目"