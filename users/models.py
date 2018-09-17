from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        image_to_save = Image.open(self.image.path)

        if image_to_save.height > 300 or image_to_save.width > 300:
            output_size = (300, 300)
            image_to_save.thumbnail(output_size)
            image_to_save.save(self.image.path)