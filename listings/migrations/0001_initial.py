# Generated by Django 4.0.5 on 2022-10-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('brand', models.CharField(max_length=150)),
                ('used', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]