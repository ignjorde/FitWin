# Generated by Django 4.1.1 on 2023-03-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_announcement_category_client_trainer_delete_anuncio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Categoria'),
        ),
    ]
