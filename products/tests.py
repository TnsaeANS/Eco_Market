from django.test import TestCase
from models import ProductImage
from models import Profile
from django.core.exceptions import ValidationError

# Create your tests here.


class ProductImageTestCases(TestCase):
    def test_char(self):
        test_ProductImage = ProductImage(product="", image="")

        with self.assertRaises(ValidationError):
            test_ProductImage.full_clean()


class ProfileTestCases(TestCase):
    def test_char(self):
        test_Profile = Profile(username="", bio="", email="")

        with self.assertRaises(ValidationError):
            test_Profile.full_clean()
