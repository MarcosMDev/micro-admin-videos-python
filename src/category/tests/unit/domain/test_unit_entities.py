from dataclasses import is_dataclass
from datetime import datetime
import unittest

from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):  # sourcery skip: extract-duplicate-method
        category1 = Category(name="Movie")
        self.assertEqual(category1.name, "Movie")
        self.assertEqual(category1.description, None)
        self.assertEqual(category1.is_active, True)
        self.assertIsInstance(category1.created_at, datetime)

        created_at = datetime.now()
        category2 = Category(
            name="Movie",
            description="some description",
            is_active=False,
            created_at=created_at,
        )
        self.assertEqual(category2.name, "Movie")
        self.assertEqual(category2.description, "some description")
        self.assertEqual(category2.is_active, False)
        self.assertEqual(category2.created_at, created_at)

    def test_if_created_at_generated_in_constructor(self):
        category1 = Category(name="Movie 1")
        category2 = Category(name="Movie 2")

        self.assertNotEqual(
            category1.created_at.timestamp(), category2.created_at.timestamp()
        )
