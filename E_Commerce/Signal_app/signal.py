from django.contrib.auth.signals import user_logged_in #signal
from django.dispatch import receiver #decorator

from django.core.signals import request_finished,request_started,got_request_exception

from django.contrib.auth.models import User #sender


#reciever function
def login_success(sender,request,user,**kwargs):
    print("I am logged in signal's reciver function")
    print(f"sender {sender}")
    print(f"User {user.username} has logged in.")
    print(f"User {user.email} email")
    print(f"Request: {request}")
    print(f"kwargs: {kwargs}")

    #i can write logic to send email to the user user.email


user_logged_in.connect(login_success,sender=User)


@receiver(got_request_exception)
def gre_reciever(sender,request,**kwargs):
    print("I am request ecxecption signal")
    print(f"sender {sender}")
    print(f"Request: {request}")
    print(f"kwargs: {kwargs}")