from django.db import models

# Create your models here.

# key attributes for login system 

#username, passwords, name, email, country


class LoginSystem(models.Model):
    username = models.CharField(max_length=25) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    Immigration_Status = models.BooleanField(default=False)
    password = models.CharField(max_length=25)

    def __str__(self):
        return f" {self.first_name} {self.last_name} {self.username}"



    