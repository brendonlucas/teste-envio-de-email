from django.db import models


class LinksRecuperacao(models.Model):
    corpo_link = models.CharField(max_length=255, null=True)
    data = models.DateField(auto_now=True)
    status = models.BooleanField(default=1)
    # relacao com um perfil email

