from django.shortcuts import render, redirect
from .models import MemorialPost


def memorial_home(request):
    """
    The main hub view. Handles displaying the tribute timeline,
    calculating the global candle counter, and saving new guest posts.
    """
    # 1. If someone fills out the form and clicks submit
    if request.method == "POST":
        author = request.POST.get("author_name")
        relationship_type = request.POST.get("relationship")
        text = request.POST.get("tribute_text")

        # Check if they ticked the "light a candle" box
        candle_ticked = request.POST.get("light_candle") == "on"

        # Save this into the database
        MemorialPost.objects.create(
            author_name=author,
            relationship=relationship_type,
            tribute_text=text,
            light_candle=candle_ticked
        )

        # Refresh the page so they immediately see their post on the timeline
        return redirect('home')

    # 2. If someone just loads the website
    # Fetch all memories from newest to oldest
    all_tributes = MemorialPost.objects.all().order_by('-date_created')

    # Count how many virtual candles have been lit
    total_candles = MemorialPost.objects.filter(light_candle=True).count()

    # Prepare to send to HTML created the context
    context = {
        'tributes': all_tributes,
        'candle_count': total_candles,
    }

    # Deliver the webpage to the visitors browser
    return render(request, 'tracker/index.html', context)
