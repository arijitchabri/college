# Generated by Django 3.2.7 on 2021-10-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteBCA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteBSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteMSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
