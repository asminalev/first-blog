# Generated by Django 2.1 on 2018-08-03 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=50)),
                ('building_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.IntegerField()),
                ('house_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.FloatField()),
                ('item_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.House')),
            ],
        ),
    ]
