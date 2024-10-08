# Generated by Django 5.1 on 2024-09-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=11)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=30)),
                ('branch', models.CharField(choices=[('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Dhaka', 'Dhaka'), ('Barisal', 'Barisal'), ('Sylhet', 'Sylhet')], default='Rajshahi', max_length=30)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
