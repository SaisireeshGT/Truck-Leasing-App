from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignForm
from .forms import ContactDealerForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:4]  # Get the first 4 unsold items
    categories = Category.objects.all()  # Get all categories

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })
def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignForm()
    return render(request, 'core/signup.html', {'form': form})

def contact_dealer(request):
    if request.method == 'POST':
        form = ContactDealerForm(request.POST)
        if form.is_valid():
            # Handle form submission
            form.save()
            return redirect('core:index')  # Redirect after successful form submission
    else:
        item_name = 'Default Item'  # Replace 'Default Item' with the actual item name
        form = ContactDealerForm(initial={'item_name': item_name})  # Pass initial data to the form
    return render(request, 'core/contact_dealer.html', {'form': form, 'item_name': item_name})

