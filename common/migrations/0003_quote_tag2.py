# Generated by Django 3.2.8 on 2021-11-01 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20211101_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='tag2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.subdepartment'),
        ),
    ]
