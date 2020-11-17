# Generated by Django 3.1.3 on 2020-11-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(choices=[('regular', 'regular'), ('square', 'square')], default='regular', max_length=7)),
                ('pizza_size', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='medium', max_length=7)),
                ('toppings', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]