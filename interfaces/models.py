from django.db import models


# Create your models here.
# 一个项目中有多个接口，那么需要在多的一侧
# 创建外键
# 父（一） 子（多）
class Interfaces(models.Model):
    name = models.CharField(max_length=100, verbose_name="接口名称", help_text="接口名称", unique=True)
    tester = models.CharField(max_length=50, verbose_name="测试人员", help_text="测试人员")
    developer = models.CharField(max_length=50, verbose_name="开发人员", help_text="开发人员")
    # null 设置该字段允许为空， blank用于设置前端可以不传递
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, default="", null=True)
    # 第一个参数为关联的模型路径或者模型类
    # 第二个参数设置的是 当父表删除之后，该字段的处理方式
    # CASECADE -》 如果父表被删除，子表该字段也会被删除
    # SET_NULL  当前外键 会被设置为None
    # PROJECT - 会报错
    # SET_DEFAULT  会设置默认值，同时需要指定 磨人值， null=True
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
                                verbose_name="所属项目", help_text="所属项目")
    # 用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_interfaces'
        # 会在admin站点中，显示一个更人性化的表明
        verbose_name = "接口"
        verbose_name_plural = "接口"
