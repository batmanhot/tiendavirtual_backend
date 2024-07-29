# Generated by Django 5.0.7 on 2024-07-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0006_rename_datospedidoid_itemspedido_datospedidoid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datospedido',
            options={'ordering': ['-id'], 'verbose_name': 'Cliente Solicitante', 'verbose_name_plural': 'Clientes Solicitantes'},
        ),
        migrations.AlterModelOptions(
            name='infonegocio',
            options={'verbose_name': 'Dato del Negocio', 'verbose_name_plural': 'Datos del Negocio'},
        ),
        migrations.AlterModelOptions(
            name='itemspedido',
            options={'ordering': ['-id'], 'verbose_name': 'Pedido Realizado', 'verbose_name_plural': 'Pedidos Realizados'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['titulo'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='datospedido',
            name='fechaHoraAtendido',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='datospedido',
            name='pedidoatendido',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='datospedido',
            name='totalItems',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='datospedido',
            name='totalPedido',
            field=models.FloatField(),
        ),
    ]
