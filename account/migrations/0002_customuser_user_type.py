# Generated by Django 5.1 on 2024-09-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=10),
        ),
    ]
