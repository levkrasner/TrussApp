from django.test import TestCase
from newApp.models import Tenant
import  views

class TenantViewTest(TestCase):
    def setUp(self):
        Tenant.objects.create(first_name = 'Lev', last_name = 'Krasner')

    def test_get_all_tenants(self):
        result = views.get_all_tenants('')
        self.assertEquals(result.items().count('Tenant'),1)
        