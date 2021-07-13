from django.contrib.auth.models import User
from instaapp.views import profile
from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.prof= Profile(bio = 'My Bio')
        self.prof.save()

    def test_save_profile(self):
        self.prof.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_profile(self):
        self.prof.save_profile()
        self.prof.delete_profile()
        profile =Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.img= Image(name = 'Cars')
        self.img.save()

    def test_retrieve_images(self):
        image=Image.retrieve_images(self)
        self.assertTrue(len(image) == 1)

    def test_update_image(self):
        image = Image.retrieve_images(self)
        image.update_image('Cars')
        image=Image.retrieve_images(self.id)
        self.assertTrue(image.name == 'Cars')

    def test_save_image(self):
        self.img.save_image()
        image=Image.objects.all()
        self.assertTrue(len(image)>0)

    def test_delete_image(self):
        self.img.save_image()
        self.img.delete_image()
        image =Image.objects.all()
        self.assertTrue(len(image) == 0)