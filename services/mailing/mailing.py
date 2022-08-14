from django.core.mail import EmailMessage
from pathlib import Path
from django.conf import settings
from django.template import Template, Context


def send_mail(subject: str, body: str, to: list) -> int:
    message = EmailMessage(subject, body, 'noreply@gmail.com', to=to)
    return message.send()


def send_html_template(subject: str, template_path: Path, context: dict, to: list) -> int:
    TEMPLATES_DIR = settings.TEMPLATES[0]['DIRS'][0]
    with open(TEMPLATES_DIR / template_path, 'r') as f:
        template = Template(f.read())

    message = EmailMessage(subject, template.render(Context(context)), 'noreply@gmail.com', to=to)
    message.content_subtype = 'html'
    return message.send()
