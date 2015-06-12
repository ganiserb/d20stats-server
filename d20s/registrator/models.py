from django.db import models
from django.contrib.auth.models import User


class Roll(models.Model):
    """
    This represents a single roll entry
    """
    roll = models.PositiveSmallIntegerField(
        verbose_name='roll number',
        help_text='The number rolled on the d20 dice'
    )
    player = models.ForeignKey(
        User,
        help_text='The player that made the roll'
    )
    moment_rolled = models.DateTimeField(
        auto_now_add=True,
        help_text='The moment the roll was registered'
    )