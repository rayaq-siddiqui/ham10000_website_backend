# Generated by Django 3.1.14 on 2022-02-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
