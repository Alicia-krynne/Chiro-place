# Generated by Django 3.2.5 on 2021-07-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_rename_produce_type_produce_produce_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone_number',
            field=models.CharField(max_length=255),
        ),
    ]