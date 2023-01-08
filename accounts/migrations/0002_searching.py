# Generated by Django 3.2.12 on 2022-04-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='searching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_search', models.CharField(max_length=100)),
                ('departure_search', models.TextField()),
                ('arrival_search', models.TextField()),
                ('budget_search', models.IntegerField()),
            ],
        ),
    ]
