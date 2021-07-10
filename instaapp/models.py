from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to='Images/')
    name=models.CharField(max_length=250, blank=True)
    caption=models.CharField(max_length=250,blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-pk']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def retrieve_images(cls):
        images=cls.objects.all()
        return images

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


