# Generated by Django 3.1.8 on 2021-11-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='veri',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
