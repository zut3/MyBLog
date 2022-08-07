from django.core.mail import EmailMessage


def send_mail(subject: str, body: str, to: list) -> int:
    message = EmailMessage(subject, body, None, to=to)
    return message.send()
