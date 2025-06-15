from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageFieldFile


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):

        user: User = self.user
        return f'{user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image: ImageFieldFile = self.image
        if image and image.path:
            img = Image.open(image.path)
            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(image.path)
