from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect


def contact(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        messages.error(request, 'Please fill all the fields')
        return redirect('home')

    email_subject = 'New message from ' + name
    email_body = 'Name: ' + name + '\nEmail: ' + email + '\nMessage: ' + message

    try:
        send_mail(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECIPIENT_EMAIL],
            fail_silently=False,
        )
        messages.success(request, 'Message sent successfully')

    except Exception as e:
        messages.error(request, 'Message not sent')
        print(e)

    return redirect('home')