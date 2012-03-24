from django.test import TestCase

from models import Noun

class NounTests(TestCase):
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

    def tearDown(self):
        self.noun0.delete()

class ViewTests(TestCase):
    def setUp(self):
        self.noun0 = Noun.objects.create(noun='potato') 

    def test_render_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_shorten_url(self):
        response0 = self.client.post('/')
        self.assertEquals(response0.status_code, 400)

        url = 'http://example.com'
        response1 = self.client.post('/', {'url': url})
        self.assertEquals(response1.status_code, 200)
        self.noun0 = Noun.objects.get(noun='potato')
        self.assertEquals(self.noun0.url, url)

        self.noun0.active = False
        self.noun0.url = ""
        self.noun0.save()

    def test_follow_redirect(self):
        url = 'http://example.com'
        self.noun0.url = url
        self.noun0.active = True
        self.noun0.save()

        response0 = self.client.get('/potato')
        self.assertRedirects(response0, url)
        self.noun0.url = url
        self.noun0.active = False
        
        response1 = self.client.get('/potato')
        self.assertEqual(response1.status_code, 404)

        self.noun0.url = ''
        self.noun0.active = False
        self.noun0.save()

    def tearDown(self):
        self.noun0.delete()
