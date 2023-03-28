# Generated by Django 4.1.7 on 2023-03-28 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Categoria')),
                ('types', models.CharField(choices=[('difficulty', 'Difficulty'), ('objectives', 'Objectives'), ('recovery', 'Recovery')], default='difficulty', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_calendar_id', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('place', models.CharField(max_length=250, verbose_name='Lugar')),
                ('price', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('finish_date', models.DateTimeField(verbose_name='Fecha de fin')),
                ('invitation_sent', models.BooleanField(default=False)),
                ('google_calendar_event_id', models.CharField(blank=True, max_length=120, null=True)),
                ('categories', models.ManyToManyField(blank=True, to='announcements.category')),
                ('clients', models.ManyToManyField(blank=True, to='users.client')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.trainer')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
        ),
    ]
