# Generated by Django 3.2.7 on 2021-09-17 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('subject_name', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=20, null=True)),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('cat', models.CharField(max_length=20)),
            ],
        ),
    ]
