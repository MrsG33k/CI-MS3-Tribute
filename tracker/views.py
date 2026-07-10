from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
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
            light_candle=candle_ticked,
            session_id=request.session.session_key
        )

        # Refresh the page so they immediately see their post on the timeline
        return redirect('home')

    # 2. If someone just loads the website (or uses the search bar)
    # Fetch all memories from newest to oldest
    all_tributes = MemorialPost.objects.all().order_by('-date_created')

    # Get the search query from the GET request
    search_query = request.GET.get('q')

    if search_query:
        # Filter the tributes based on the search query
        all_tributes = all_tributes.filter(
            Q(author_name__icontains=search_query) |
            Q(tribute_text__icontains=search_query)
        )

    # Count how many virtual candles have been lit
    total_candles = MemorialPost.objects.filter(light_candle=True).count()

    # Prepare to send to HTML created the context
    context = {
        'tributes': all_tributes,
        'candle_count': total_candles,
        'user_session_key': request.session.session_key
    }

    # Deliver the webpage to the visitors browser
    return render(request, 'tracker/index.html', context)


def edit_tribute(request, pk):
    """View to handle updating a tribute from the front end"""
    tribute = get_object_or_404(MemorialPost, pk=pk)

    # Security check: Ensure the session
    # trying to edit matches the author's session
    if tribute.session_id != request.session.session_key:
        return redirect('home')

    if request.method == 'POST':
        tribute.author_name = request.POST.get('author_name')
        tribute.relationship = request.POST.get('relationship')
        tribute.tribute_text = request.POST.get('tribute_text')
        tribute.light_candle = request.POST.get('light_candle') == 'on'
        tribute.save()
        return redirect('home')

    return render(request, 'tracker/edit_tribute.html', {'tribute': tribute})


def delete_tribute(request, pk):
    """View to handle removing a tribute from the front end"""
    tribute = get_object_or_404(MemorialPost, pk=pk)

    # Security check: Ensure the session trying to
    # delete matches the author's session
    if tribute.session_id == request.session.session_key:
        tribute.delete()

    return redirect('home')
