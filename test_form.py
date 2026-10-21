import unittest
import os
import re

class TestHTMLForm(unittest.TestCase):
    def setUp(self):
        # Ensure file exists before running checks
        self.assertTrue(os.path.exists("index.html"), "Error: index.html file not found!")
        with open("index.html", "r", encoding="utf-8") as file:
            self.content = file.read()

    def test_form_tag_present(self):
        self.assertRegex(self.content, r"<form[\s\S]*?>", "Form tag is missing")

    def test_name_field_present(self):
        self.assertTrue(
            bool(re.search(r'name=["\']name["\']', self.content)),
            "Name input field is missing"
        )

    def test_email_field_present(self):
        self.assertTrue(
            bool(re.search(r'type=["\']email["\']', self.content)),
            "Email input field is missing"
        )

    def test_contact_field_present(self):
        self.assertTrue(
            bool(re.search(r'name=["\']contact["\']', self.content)),
            "Contact number input field is missing"
        )

    def test_submit_button_present(self):
        self.assertTrue(
            bool(re.search(r'type=["\']submit["\']', self.content)),
            "Submit button is missing"
        )

if __name__ == '__main__':
    unittest.main()
