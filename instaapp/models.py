from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Image(models.Model):
    image=models.ImageField(upload_to='Images/')
    name=models.CharField(max_length=250, blank=True)
    caption=models.CharField(max_length=250,blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    
    


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


class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ["-pk"]




