# Generated by Django 3.0.4 on 2020-05-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200411_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predmeti',
            name='bodovi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
