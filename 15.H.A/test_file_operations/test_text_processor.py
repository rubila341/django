import unittest
from text_processor import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.text1 = "Hello, World!"
        self.text2 = "123 ABC!!!"
        self.text3 = "this is a test"
        self.text4 = "hello world"
        self.processor1 = TextProcessor(self.text1)
        self.processor2 = TextProcessor(self.text2)
        self.processor3 = TextProcessor(self.text3)
        self.processor4 = TextProcessor(self.text4)

    def test_clean_text_removes_non_alpha_characters(self):
        self.processor1.clean_text()
        self.assertEqual(self.processor1.cleaned_text, "hello world")

    def test_clean_text_lowercase_conversion(self):
        self.processor2.clean_text()
        self.assertEqual(self.processor2.cleaned_text, "abc")

    def test_clean_text_empty_string(self):
        empty_processor = TextProcessor("")
        empty_processor.clean_text()
        self.assertEqual(empty_processor.cleaned_text, "")

    def test_remove_stop_words(self):
        self.processor3.clean_text()
        self.processor3.remove_stop_words(['this', 'is'])
        self.assertEqual(self.processor3.cleaned_text, "a test")

    def test_remove_stop_words_clean_text_not_called(self):
        self.processor4.remove_stop_words([])
        self.assertEqual(self.processor4.cleaned_text, "hello world")

    def test_remove_stop_words_no_stop_words(self):
        self.processor4.clean_text()
        self.processor4.remove_stop_words([])
        self.assertEqual(self.processor4.cleaned_text, "hello world")

if __name__ == '__main__':
    unittest.main()
