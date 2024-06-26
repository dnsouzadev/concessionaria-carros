# Generated by Django 5.0.6 on 2024-06-14 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nivel_bruto',
            field=models.CharField(choices=[('BRONZE', 'Bronze'), ('PRATA', 'Prata'), ('OURO', 'Ouro'), ('DIAMANTE', 'Diamante')], default='BRONZE', max_length=8),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='cliente.cliente')),
            ],
        ),
    ]
