# Generated by Django 4.2.3 on 2023-08-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='recetas'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='producto',
            field=models.CharField(choices=[('Carnes', 'Carnes'), ('Verdura', 'Verdura'), ('Bebidas', 'Bebidas'), ('Pescado', 'Pescado'), ('Postres', 'Postres'), ('Pan', 'Pan')], max_length=50),
        ),
        migrations.AlterField(
            model_name='receta',
            name='dificultad',
            field=models.IntegerField(choices=[(1, 'Fácil'), (2, 'Media'), (3, 'Difícil')]),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='categoria',
            field=models.CharField(choices=[('Comida rápida', 'Comida rápida'), ('Meriendas', 'Meriendas'), ('Veggie', 'Veggie'), ('Cena', 'Cena')], max_length=50),
        ),
    ]