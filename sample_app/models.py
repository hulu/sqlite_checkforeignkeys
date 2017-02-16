from django.db import models


class Referenced(models.Model):
    pass


class Referencer(models.Model):
    fk = models.ForeignKey(Referenced)
