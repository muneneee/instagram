from django.test import TestCase
from .models import Image



class ImageTestClass(TestCase):
    
    def setUp(self):
        self.image = Image(name='jorja',caption = 'nice')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))


    def test_save_image(self):
        self.image.save_image()
        photos = Image.objects.all()
        self.assertTrue(len(photos)>0)


     def test_delete_image(self):
        self.image.test_delete_image()
        photos = Image.objects.all()
        self.assertTrue(len(photos) < 1)
