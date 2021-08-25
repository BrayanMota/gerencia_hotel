# Generated by Django 3.2.6 on 2021-08-25 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_alter_quarto_frigobar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.quarto')),
            ],
        ),
    ]