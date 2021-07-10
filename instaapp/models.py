from django.db import models

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
