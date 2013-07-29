from django.db import models

class LaunchUser(models.Model):
    name = models.CharField(u"Nome", max_length=200)
    email = models.EmailField(u"E-mail")

    def __unicode__(self):
        return self.name
