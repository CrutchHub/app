# Generated by Django 4.2.5 on 2023-12-20 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_adress_table_alter_apartment_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='HouseID',
            field=models.ForeignKey(db_column='HouseID', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.house'),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApartmentID',
            field=models.ForeignKey(db_column='ApartmentID', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.apartment'),
        ),
        migrations.AlterField(
            model_name='application',
            name='UserID',
            field=models.ForeignKey(db_column='UserID', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='AdressID',
            field=models.ForeignKey(db_column='AdressID', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.adress'),
        ),
    ]
