from django.shortcuts import redirect

def login_redirect(redirect):
    return redirect('/InfoTrack/login')

"""
from django.core.mail import send_mail
send_mail('InfoTrack:Reset Password', 'Welcome to InfoTrack!', 'compsci326326@gmail.com',
    ['qzhao@umass.com'], fail_silently=False)
"""