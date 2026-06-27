from django.db import models


class MemorialPost(models.Model):
    """
    A database table to store guestbook tributes and virtual candles
    left by family and friends for a loved one.
    """
    # Predefined relationship options for clean front-end dropdown menu
    RELATIONSHIP_CHOICES = [
        ('family', 'Family'),
        ('friend', 'Friend'),
        ('railway', 'Railway'),
        ('football', 'Football'),
        ('community', 'Community'),
        ('other', 'Other')
    ]

    # Form fields that visitors will complete
    author_name = models.CharField(max_length=100, blank=False)
    relationship = models.CharField(max_length=30,
                                    choices=RELATIONSHIP_CHOICES,
                                    default='friend')
    tribute_text = models.TextField(blank=False)

    # Virtual Candle option
    light_candle = models.BooleanField(default=False)

    # Automatically records the date and time the memory was posted
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # How the post will look inside the Django admin panel
        return f"Tribute from {self.author_name} ({self.get_relationship_display()})"  # noqa: E501
