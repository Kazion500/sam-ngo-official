# Generated by Django 3.2.3 on 2021-06-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0005_auto_20210601_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
