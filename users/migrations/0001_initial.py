# Generated by Django 3.1.2 on 2020-11-07 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'tb_role',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tb_userGroup',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('userType', models.CharField(choices=[(1, '普通用户'), (2, 'vip'), (3, 'svip')], max_length=21)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usergroup')),
                ('role', models.ManyToManyField(to='users.Role')),
            ],
            options={
                'db_table': 'tb_userInfo',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.userinfo')),
            ],
            options={
                'db_table': 'tb_userToken',
            },
        ),
    ]
