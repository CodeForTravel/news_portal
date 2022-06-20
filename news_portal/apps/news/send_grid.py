import logging
import sendgrid
import os
from sendgrid.helpers.mail import Mail
from django.conf import settings

logger = logging.getLogger(__name__)


def send_mail(user, message_body, message_header):
    from_email = settings.EMAIL_NOREPLY
    to_email = user.email
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=message_header,
        html_content=message_body
    )
    
    try:
        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)
        logger.info(f"SendGrid response: {response.status_code}")
    except Exception as e:
        logger.exception(e)
