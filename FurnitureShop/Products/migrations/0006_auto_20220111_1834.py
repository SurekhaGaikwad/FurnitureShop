# Generated by Django 3.2.10 on 2022-01-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20220110_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='livingroom',
            name='IMGSet1',
            field=models.CharField(default=True, max_length=2500),
        ),
        migrations.AddField(
            model_name='livingroom',
            name='IMGSet2',
            field=models.CharField(default=True, max_length=2500),
        ),
        migrations.AddField(
            model_name='livingroom',
            name='IMGSet3',
            field=models.CharField(default=True, max_length=2500),
        ),
        migrations.AddField(
            model_name='livingroom',
            name='IMGSet4',
            field=models.CharField(default=True, max_length=2500),
        ),
    ]