from django.core.validators import MinLengthValidator
from django.db import models
from Fruitipedia_App.user.validators import validate_name


class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[
            MinLengthValidator(2),
            validate_name
        ]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[
            MinLengthValidator(1),
            validate_name
        ]
    )
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
        max_length=40
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text='*Password length requirements: 8 to 20 characters',
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )

    class Meta:
        db_table = 'Users'