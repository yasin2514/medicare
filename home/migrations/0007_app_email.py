# Generated by Django 3.1.8 on 2021-11-08 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
