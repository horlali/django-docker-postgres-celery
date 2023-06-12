"""Utility for sending emails"""

import logging
import os

from celery import shared_task
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import ClickTracking, Mail, TrackingSettings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@shared_task
def send_mail(recipient: str, subject: str, content: str) -> dict[str, int] | None:
    """
    Send a plain text email using SendGrid
    params:
        receipient (str): email of the receipient
        subject (str): subject of the email to send
        content (str): content of the email to send
    return:
        status_code (dict[str, int]): a dictionary of status code.
    """
    message = Mail(
        from_email=os.getenv("SENDGRID_HOST_USER"),
        to_emails=recipient,
        subject=subject,
        plain_text_content=content,
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

        # Disabling click tracking
        tracking_settings = TrackingSettings()
        tracking_settings.click_tracking = ClickTracking(enable=True, enable_text=False)
        message.tracking_settings = tracking_settings

        response = sg.send(message)

        return {"status_code": response.status_code}

    except Exception as e:
        logger.error(f"Sendgrid is failing: {e}")
