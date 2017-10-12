from django.db import models

class Profile(models.Model):
    name = 'Hash Slinging Slasher'
    email = 'hashslinging@krustykrab.bb'
    birthday = '29 Feb'
    expertise = ["Rusty spatula", "Red eyes", "A cook", "Missing", "Ghost", "Clumsy"]
    gender = 'Unknown'
    description = "A dead Krusty Krab's cook"

    def __str__(self):
        return self.name + '(' + self.email + ')'
