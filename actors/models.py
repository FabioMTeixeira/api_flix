from django.db import models

# Create your models here.


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('Brazil', 'Brasil'),
    ('Other', 'Outros'),
)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
    )

    def __str__(self):
        return self.name
