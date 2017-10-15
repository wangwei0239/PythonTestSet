# encoding=utf-8
from unittest import TestCase


class TestArabicToChinese(TestCase):
    def test_arabic_to_chinese(self):
        import atc2
        print atc2.arabic_to_chinese(1000)
        self.assertEqual(atc2.arabic_to_chinese(1000), [u'一零零零', u'一千'])
