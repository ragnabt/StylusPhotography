from django.test import TestCase
from django.core.mail import send_mail

# Create your tests he


class TestContactPage(TestCase):
    def test_send_mail(self):
        send_mail('Test', 'Here is the message.', 'from@example.com', ['rajhona.gabor@gmail.com'], fail_silently=False)
