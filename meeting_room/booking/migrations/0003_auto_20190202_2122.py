# Generated by Django 2.1.5 on 2019-02-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190202_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='fim_reserva',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='inicio_reserva',
            field=models.DateTimeField(),
        ),
    ]
