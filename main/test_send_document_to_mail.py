from unittest import TestCase
from main import starter


class TestSend_document_to_mail(TestCase):
    def test_send_document_to_mail(self):
        f = open('Hello.docx', 'rb')
        result = starter.send_document_to_mail('tsydimasik@gmail.com', 'subject', f)
        f.close()
        assert result is True

    def test_generate_document(self):
        print('do smths...')
