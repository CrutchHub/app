# Generated by Django 4.2.5 on 2024-05-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_apartment_apartmentnumber_alter_apartment_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='Model3D',
            field=models.FileField(default=0, upload_to='3d_models'),
            preserve_default=False,
        ),
    ]