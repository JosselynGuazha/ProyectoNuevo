# Generated by Django 3.2 on 2021-05-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Apellidos y Nombres/Razón Social')),
                ('author', models.CharField(max_length=100, verbose_name='Apellidos y Nombres/Razón Social')),
                ('price', models.CharField(max_length=100, verbose_name='Apellidos y Nombres/Razón Social')),
            ],
        ),
    ]
