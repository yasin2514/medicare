# Generated by Django 3.1.8 on 2021-11-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='schedule_day',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='schedule_time',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
