from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def place_list(request):
    """If this is a POST request, the user clicked the Add button in
    the form. Chrvk if the new place is valid, if so, save a new Place to the  database, and redirect to this same page.
    This creates a GET request to this same route.
    
    If not a POST route, or Place is not valid, display a page with a list of places and a form to add a new place.
    """

    if request.method == 'POST':
        # create new place    
        form = NewPlaceForm(request.POST)  # creating form from form data in request
        place = form.save(commit=False)# creating a model objecct from  form
        place.user = request.user
        if form.is_valid(): # validating against DB constraints
            place.save() # saves place to db
            return redirect('place_list') # reloads home page

    # if not a POST, or the form is not valid, render the page
    #with the form to add a new place, and list of places
    places = Place.objects.filter(user=request.user).filter(visited=False). order_by('name')
    new_place_form = NewPlaceForm() #used to create HTML
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })


@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        #place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.visited = True
            place.save() #changes made in code are not reflected in db unless saved
        else:
            return HttpResponseForbidden()

    return redirect ('place_list')

@login_required
def place_details(request,place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    return render(request, 'travel_wishlist/place_detail.html', {'place':place})

@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden()


""" def about (request):
    author = 'Christian'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about}) """