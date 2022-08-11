from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.urls import reverse


class UserCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d", default='placeholder.png')
    user_name = models.CharField(max_length=255)
    user_status = models.ForeignKey(UserCategory, on_delete=models.CASCADE, default=1)
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        super().save()

        def crop_center(pil_img, crop):
            img_width, img_height = pil_img.size
            return pil_img.crop(((img_width - crop) // 2,
                             (img_height - crop) // 2,
                             (img_width + crop) // 2,
                             (img_height + crop) // 2))

        img = Image.open(self.avatar.path)
        img_new = crop_center(img, min(img.size))
        img_new.save(self.avatar.path)

    def get_absolute_url(self):
        return reverse('User', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.user_name = "User" + str(instance.userprofile.pk)
    instance.userprofile.save()


class Level(models.Model):
    nr_level = models.IntegerField()
    description_level = models.CharField(max_length=255,  blank=True, null=True)

    def get_absolute_url(self):
        return reverse('Level', kwargs={'lvl': self.pk})
