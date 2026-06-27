from django.contrib import admin
from .models import MemorialPost

# Register the model so it can be managed in the Admin Dashboard


@admin.register(MemorialPost)
class MemorialPostAdmin(admin.ModelAdmin):
    # Determines what details admin see when looking at list of posts
    list_display = ('author_name', 'relationship',
                    'light_candle', 'date_created')

    # Adds a filter for easier viewing
    list_filter = ('light_candle', 'relationship', 'date_created')

    # Allows searching on certain fields
    search_fields = ('author_name', 'tribute_text')
