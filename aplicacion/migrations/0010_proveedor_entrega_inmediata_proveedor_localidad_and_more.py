# Generated by Django 4.2.3 on 2023-08-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_remove_restaurante_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='entrega_inmediata',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='localidad',
            field=models.CharField(default='Córdoba', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='metodos_pago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('Transferencia', 'Transferencia'), ('Todos', 'Todos')], default='Efectivo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='sitio_web',
            field=models.CharField(default='www.panaderiaroma.com', max_length=50),
            preserve_default=False,
        ),
    ]
