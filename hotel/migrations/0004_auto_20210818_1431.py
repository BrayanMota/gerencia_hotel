# Generated by Django 3.2.6 on 2021-08-18 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20210816_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='nome',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quarto',
            name='numero',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='preco',
            field=models.FloatField(blank=True),
        ),
    ]
