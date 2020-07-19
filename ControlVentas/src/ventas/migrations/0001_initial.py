# Generated by Django 3.0.8 on 2020-07-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('cliente', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precioU', models.DecimalField(decimal_places=2, max_digits=9)),
                ('precioV', models.DecimalField(decimal_places=2, max_digits=9)),
                ('pago', models.CharField(choices=[('contado', 'CONTADO'), ('credito', 'CREDITO')], default='contado', max_length=10)),
                ('fecha', models.DateField(blank=True)),
            ],
        ),
    ]
