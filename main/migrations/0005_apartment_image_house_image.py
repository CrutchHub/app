# Generated by Django 4.2.5 on 2023-12-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_apartment_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]