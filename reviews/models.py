from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

# Create your models here.


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.FloatField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser menor que zero'),
            MaxValueValidator(5, 'Avaliação não pode ser maior que cinco'),
        ]
    )
    comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'Review de {self.movie.name} - {self.stars} estrelas'
