# Generated by Django 5.0.6 on 2024-05-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cnic',
            field=models.CharField(default='cnic', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='yourname', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='phone', max_length=100),
            preserve_default=False,
        ),
    ]
