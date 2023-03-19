
# Generated by Django 4.1.7 on 2023-03-13 22:52


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='finish_date',
            field=models.DateTimeField(verbose_name='Fecha de fin'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='start_date',
            field=models.DateTimeField(verbose_name='Fecha de inicio'),
        ),
    ]
