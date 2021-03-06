# Generated by Django 2.2.9 on 2020-01-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200121_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='mobile_no',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='profilePicture',
            field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
