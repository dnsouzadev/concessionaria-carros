# Generated by Django 5.0.6 on 2024-06-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='carros'),
        ),
    ]
