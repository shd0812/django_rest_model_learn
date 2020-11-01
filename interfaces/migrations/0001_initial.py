# Generated by Django 3.1.2 on 2020-11-01 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='接口名称', max_length=100, unique=True, verbose_name='接口名称')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('developer', models.CharField(help_text='开发人员', max_length=50, verbose_name='开发人员')),
                ('desc', models.TextField(blank=True, default='', help_text='简要描述', null=True, verbose_name='简要描述')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='projects.projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口',
                'db_table': 'tb_interfaces',
            },
        ),
    ]
