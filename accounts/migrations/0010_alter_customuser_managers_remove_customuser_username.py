# Generated by Django 4.0.5 on 2022-06-14 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
