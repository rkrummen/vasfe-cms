# Generated by Django 2.1.2 on 2019-06-23 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190619_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
