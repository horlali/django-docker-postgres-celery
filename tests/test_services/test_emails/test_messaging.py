from unittest.mock import patch

from django.test import TestCase

from services.emails.messaging import send_mail


class TestSendMail(TestCase):
    def setUp(self):
        self.test_email_data = {
            "recipient": "test@example.com",
            "subject": "Test Subject",
            "content": "Test Content",
        }

    @patch("services.emails.messaging.SendGridAPIClient")
    def test_send_mail_success(self, mock_sendgrid):
        mock_sendgrid.return_value.send.return_value.status_code = 202
        result = send_mail(**self.test_email_data)

        self.assertEqual(result, {"status_code": 202})

    @patch("services.emails.messaging.SendGridAPIClient")
    def test_send_mail_failure(self, mock_sendgrid):
        mock_sendgrid.return_value.send.side_effect = Exception("SendGrid API error")
        result = send_mail(**self.test_email_data)

        self.assertIsNone(result)
