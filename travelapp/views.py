from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# def index(request):
#     return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# def fyp(request):
#     return render(request,'fyp.html')

def service(request):
    return render(request,'service.html')

def login(request):
    return render(request,'login.html')

def recomendations(request):
    return render(request,'recomendations.html')

def contact(request):
    return render(request,'contact.html')

def userdash(request):
    return render(request,'userdash.html')

def favlocation(request):
    return render(request,'favlocation.html')

def recentrecom(request):
    return render(request,'recentrecom.html')

def support(request):
    return render(request,'support.html')

def testimonial(request):
    return render(request,'testimonial.html')

def profile(request):
    return render(request,'profile.html')

def package(request):
    return render(request,'package.html')



#user registration
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirmpassword = request.POST.get('confirm_password', '')

        if not username or not email or not password  or not confirmpassword:
            messages.error(request, 'Please fill all the fields.')
        elif password != confirmpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('register_view')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login_view')

    return render(request, 'login.html', {'page': 'register'})


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')  # Adjust 'index' to the name of your home page view
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'page': 'login'})

    #Testimonial form
# from .forms import testform
# # from .models import Test
# def testimonial(request):
#         if request.method == 'POST':
#             form = testform(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('testimonial')
#         else:
#             form = testform()
#         return render(request,'review.html',{'form':form})   

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        location = request.POST.get('location', '').strip()
        review = request.POST.get('review', '').strip()

        # Validate fields
        if not all([name, email, location, review]):
            messages.error(request, 'Please fill all the fields.')
        else:
            try:
                validate_email(email)
                # Save to database
                Test.objects.create(name=name, email=email, location=location, review=review)
                messages.success(request, 'Review submitted successfully.')
                return redirect('index')
            except ValidationError:
                messages.error(request, 'Invalid email address.')
            except Exception as e:
                messages.error(request, 'An error occurred. Please try again.')

    return render(request, 'index.html') 

# from django.shortcuts import render, redirect
# from .forms import TourPreferenceForm

# def filter_tours(request):
#     if request.method == 'POST':
#         form = TourPreferenceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Filters applied successfully!')
#             return redirect('recomendations')  # Adjust this if needed
#     else:
#         form = TourPreferenceForm()
    
#     return render(request, 'recomendations.html', {'form': form})

  #search
from django.shortcuts import render
from .models import Destination
from django.db.models import Q
@login_required(login_url='login_view')
def search_destinations(request):
    query = request.GET.get('query', '').strip()  # Get user input and strip any extra spaces
    destinations = None

    if query:
        destinations = Destination.objects.filter(
            Q(location__icontains=query) | Q(name__icontains=query) | Q(tour_type__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(continent__icontains=query) | Q(interest__icontains=query)  
        )
    else:
        destinations = None  # or you could display all destinations here, depending on your preference

    return render(request, 'search.html', {'destinations': destinations, 'query': query})




# from django.shortcuts import render
# from .models import Destination

# @login_required(login_url='login_view')
# def filter_destinations(request):
#     destinations = None  # Initially no results

 
#     tour_type = request.GET.get('tour_type')
#     accommodation_type = request.GET.get('accommodation_type')
#     state = request.GET.get('state')
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')
#     max_days = request.GET.get('max_days') 
#     interest = request.GET.get('interest')
#     min_distance = request.GET.get('min_distance')
#     max_distance = request.GET.get('max_distance')

#     if any([tour_type, accommodation_type, state, min_price, max_price, max_days, interest, min_distance, max_distance]):
#         destinations = Destination.objects.all()

#         # Apply filters
#         if tour_type:
#             destinations = destinations.filter(tour_type=tour_type)

#         if accommodation_type:
#             destinations = destinations.filter(accommodation_type=accommodation_type)

#         if state:
#             destinations = destinations.filter(state__icontains=state)

#         if min_price and max_price:
#             destinations = destinations.filter(price__gte=min_price, price__lte=max_price)

#         if max_days:
#             destinations = destinations.filter(duration__lte=max_days)

#         if interest:
#             destinations = destinations.filter(interest__icontains=interest)

#         if min_distance and max_distance:
#             destinations = destinations.filter(distance__gte=min_distance, distance__lte=max_distance)

#     return render(request, 'recomendations.html', {'destinations': destinations})

# from django.shortcuts import render
# from .models import contact

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '').strip()
#         email = request.POST.get('email', '').strip()
#         subject = request.POST.get('subject', '')
#         message = request.POST.get('message', '')

#         if not all([name, email, subject, message]):
#             messages.error(request, 'Please fill all the fields.')
#         else:
#             contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
#             messages.success(request, 'Message sent successfully.')
#             return redirect('contact')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not (name and email and subject and message):
            messages.error(request, 'All fields are required.')
        else:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')

    return render(request, 'contact.html')
from django.shortcuts import render
from .models import Destination

# def personalized_recommendations(request):
#     user_interest = request.GET.get('interest', None)

#     # Start with all destinations
#     destinations = Destination.objects.all()

#     # Apply filtering only if interest is provided
#     if user_interest:
#         destinations = destinations.filter(interest__icontains=user_interest)

#     return render(request, 'test.html', {'destinations': destinations})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Destination, Favorite


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favorite, Destination

@login_required
def add_to_favorites(request, destination_id):
    """Adds a destination to the user's favorites if not already added."""
    destination = get_object_or_404(Destination, id=destination_id)

    # Check if the destination is already in favorites
    if Favorite.objects.filter(user=request.user, destination=destination).exists():
        messages.warning(request, f'{destination.name} is already in your favorites.')
    else:
        Favorite.objects.create(user=request.user, destination=destination)
        messages.success(request, f'Added {destination.name} to favorites!')

    return redirect('view_favorites')  # Redirect to favorites page

@login_required
def view_favorites(request):
    """Displays the user's favorite destinations."""
    favorites = Favorite.objects.filter(user=request.user).select_related('destination')
    return render(request, 'favorites.html', {'favorites': favorites})
@login_required
def remove_favorite(request, destination_id):
    """Removes a destination from the user's favorites."""
    destination = get_object_or_404(Destination, id=destination_id)
    Favorite.objects.filter(user=request.user, destination=destination).delete()
    messages.info(request, f'Removed {destination.name} from favorites.')
    return redirect('view_favorites')
import pandas as pd
import numpy as np
from django.shortcuts import render
from django.db.models import Sum
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Destination,  Favorite
from django.core.exceptions import ValidationError


def personalized_recommendations(request):
    user = request.user if request.user.is_authenticated else None  # Check if the user is logged in

    # Fetch user's favorite destinations
    favorite_destinations = Favorite.objects.filter(user=user).values_list('destination__id', flat=True)

    # Fetch all destinations
    destinations = Destination.objects.all()
    
    if not destinations.exists():
        return render(request, 'test.html', {'destinations': []})  # If no destinations exist

    # Create a DataFrame of destinations
    data = pd.DataFrame(list(destinations.values('id', 'name', 'location', 'tour_type', 'interest', 'description')))

    # Fill NaN values
    data.fillna("", inplace=True)

    # Combine all text features to create a "content" column
    data["content"] = (
        data["name"] + " " + data["location"] + " " + data["tour_type"] + " " + data["interest"] + " " + data["description"]
    )

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(data["content"])

    recommended_ids = set()

    # **Find Similar Destinations Based on User's Favorites**
    if favorite_destinations:
        fav_vectors = tfidf_matrix[data.index[data["id"].isin(favorite_destinations)]]
        similarity_scores = cosine_similarity(fav_vectors, tfidf_matrix).mean(axis=0)
        top_indices = similarity_scores.argsort()[-5:][::-1]  # Get top 5 matches
        recommended_ids.update(data.iloc[top_indices]["id"].tolist())

    # Get final recommended destinations
    recommended_destinations = Destination.objects.filter(id__in=recommended_ids)[:5]

    return render(request, 'fyp.html', {'destinations': recommended_destinations})
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Destination

@login_required(login_url='login_view')
def filter_destinations(request):
    destinations = None  # Initially no results

    # Get filter options from request
    tour_type = request.GET.get('tour_type')
    accommodation_type = request.GET.get('accommodation_type')
    state = request.GET.get('state')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    max_days = request.GET.get('max_days') 
    interest = request.GET.get('interest')
    min_distance = request.GET.get('min_distance')
    max_distance = request.GET.get('max_distance')

    if any([tour_type, accommodation_type, state, min_price, max_price, max_days, interest, min_distance, max_distance]):
        destinations = Destination.objects.all()

        # Apply filters
        if tour_type:
            destinations = destinations.filter(tour_type=tour_type)

        if accommodation_type:
            destinations = destinations.filter(accommodation_type=accommodation_type)

        if state:
            destinations = destinations.filter(state__icontains=state)

        if min_price and max_price:
            destinations = destinations.filter(price__gte=min_price, price__lte=max_price)

        if max_days:
            destinations = destinations.filter(duration__lte=max_days)

        if interest:
            destinations = destinations.filter(interest__icontains=interest)

        if min_distance and max_distance:
            destinations = destinations.filter(distance__gte=min_distance, distance__lte=max_distance)

        

    return render(request, 'recomendations.html', {'destinations': destinations})

