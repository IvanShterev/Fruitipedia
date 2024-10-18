from django.db import models
from django.core.validators import MinLengthValidator
from Fruitipedia_App.fruit.validators import validate_name
from Fruitipedia_App.user.models import Profile


class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            validate_name
        ],
        error_messages={
            'unique': "This fruit name is already in use! Try a new one."
        }
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='fruits'
    )

    class Meta:
        db_table = 'Fruits'