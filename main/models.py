from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os

def get_upload_path(instance, filename):
    return os.path.join(settings.STATIC_ROOT, 'main', 'images', filename)

def save(self, *args, **kwargs):
    if not self.Image:
        self.Image = 'house_images/default.jpg'  # Замените 'default.jpg' на ваше значение по умолчанию
    super(House, self).save(*args, **kwargs)


class Adress(models.Model):
    ID = models.AutoField(primary_key=True)
    AdressText = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = 'adress'

class House(models.Model):
    ID = models.AutoField(primary_key=True)
    AdressID = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True, db_column='AdressID')
    NumberOfFloors = models.IntegerField(default=1)
    NumberOfEntrances = models.IntegerField(default=1)
    Image = models.ImageField(upload_to="images", null=True, blank=True)
    
    def get_image_url(self):
        if self.Image:
            return os.path.join(settings.STATIC_URL, self.Image.url)
        return None
    
    class Meta:
        db_table = 'house'

class Apartment(models.Model):
    ID = models.AutoField(primary_key=True)
    HouseID = models.ForeignKey(House, on_delete=models.CASCADE, null=True, db_column='HouseID')
    ApartmentNumber = models.IntegerField(default=0)
    NumberOfRooms = models.IntegerField(default=1)
    Cost = models.FloatField(default=0)
    Area = models.FloatField(default=0, null=True)
    Image = models.ImageField(upload_to="images", null=True, blank=True)
    Model3D = models.FileField(upload_to='3d_models')

    def get_image_url(self):
        if self.Image:
            return os.path.join(settings.STATIC_URL, self.Image.url)
        return None

    class Meta:
        db_table = 'apartment'

class Application(models.Model):
    ApplicationID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column='UserID')
    ApartmentID = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True , db_column='ApartmentID')
    Status = models.BooleanField(default=False)
    class Meta:
        db_table = 'application'
