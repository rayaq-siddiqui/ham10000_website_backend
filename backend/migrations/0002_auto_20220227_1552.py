# Generated by Django 3.1.14 on 2022-02-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]
