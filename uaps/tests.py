from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UAPS


class UAPSTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_uaps = UAPS.objects.create(seen_by="Bob Lazar", owner=testuser1, velocity="mk2", description="red squares")
        test_uaps.save()

    def test_uaps_model(self):
        uaps = UAPS.objects.get(id=1)
        actual_owner = str(uaps.owner)
        actual_seen_by = str(uaps.name)
        actual_velocity = str(uaps.name)
        actual_description = str(uaps.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_seen_by, "Mr. Lear")
        self.assertEqual(actual_velocity, "lightspeed")
        self.assertEqual(actual_description, "tictac")

    def test_uaps_model(self):
        test_uaps = UAPS.objects.get(id=2)
        expected_uaps_seen_by = "Bob Lazar"
        self.assertEqual(str(test_uaps), expected_uaps_seen_by)