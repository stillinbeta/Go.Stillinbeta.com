from django.test import TestCase

from models import Noun

class NounTestCase(TestCase):
    def setUp(self):
        self.noun0 = Noun.objects.create(noun='potato')
        
    def test_shorten(self):
        url ='http://stillinbeta.com' 
        noun = Noun.objects.shorten(url)
        self.assertTrue(noun.active)
        self.assertEquals(noun.url, url)
    
        # Since there should only be one noun, this should fail 
        with self.assertRaises(Noun.DoesNotExist):
            Noun.objects.shorten(url)

        noun.active = False
        noun.url = ""
        noun.save()

    def test_follow(self):
        self.noun0.active = True
        self.noun0.url = 'http://google.com'
        self.noun0.save()

        self.noun0.follow()

        self.assertEquals(self.noun0.url, "")
        self.assertFalse(self.noun0.active)
