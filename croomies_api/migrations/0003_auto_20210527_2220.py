# Generated by Django 3.2 on 2021-05-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croomies_api', '0002_alter_seeker_number_of_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeker',
            name='searching_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='searching_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]