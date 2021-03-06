# Generated by Django 2.2.5 on 2019-11-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Censado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura_LM35', models.FloatField(max_length=10)),
                ('temperatura_DS18B20', models.FloatField(max_length=10)),
                ('humedad_HL69', models.FloatField(max_length=10)),
                ('status_riego', models.IntegerField()),
                ('hora', models.DateTimeField()),
                ('anomalia', models.IntegerField()),
            ],
        ),
    ]
