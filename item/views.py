from django.shortcuts import render, get_object_or_404
from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)  # Fetch the Item object
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]  # Correct queryset
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, 'item/detail.html', context)

