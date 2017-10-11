class Profile(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    birthday = models.DateField()
    expertise =  models.TextField() # comma-separated
    gender = models.CharField(max_length=8)
    description = models.CharField(max_length=128)
    picture_url = models.URLField()

    def __str__(self):
        return self.name + '(' + self.email + ')'
