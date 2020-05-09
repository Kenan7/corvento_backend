from django.test import TestCase
from main.models import Event, Category
import factory


# class CategoryTestCase(TestCase):
#     def setUp(self):
#         Category.objects.create(name="Yazılım", icon="fa fa-whatever")
#         Category.objects.create(name="Girişimcilik", icon="fa fa-whatever")

#     def test_categories(self):
#         yazilim = Category.objects.get(name="Yazılım")
#         girisimcilik = Category.objects.get(name="Girişimcilik")
#         self.assertEqual("Yazılım", yazilim.name)


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('company')
    icon = factory.Faker('color')
