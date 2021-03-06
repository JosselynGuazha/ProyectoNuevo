# Generated by Django 3.2 on 2021-05-21 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20210520_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ice',
            field=models.CharField(blank=True, choices=[('3011', 'CIGARRILLOS RUBIOS'), ('3021', 'CIGARRILLOS NEGROS'), ('3023', 'PRODUCTOS DEL TABACO....')], max_length=50, null=True, verbose_name='ICE'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='irbpnr',
            field=models.CharField(blank=True, choices=[('5001', 'BOTELLAS PLASTICAS NO RETORNABLES')], max_length=10, null=True, verbose_name='IRBPNR'),
        ),
    ]
