from django.urls import path
from . import views
from .views import search_destinations
from .views import filter_destinations
from .views import contact_view,personalized_recommendations,add_to_favorites,view_favorites,remove_favorite

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('fyp/', views.fyp, name='fyp'),
    path('service/', views.service, name='service'),
    
    # path('recomendations/', views.recomendations, name='recomendations'),
    path('contact/', views.contact_view, name='contact'),
    path('userdash/', views.userdash, name='userdash'),
    path('favlocation/', views.favlocation, name='favlocation'),
    path('recentrecom/', views.recentrecom, name='recentrecom'),
    path('support/', views.support, name='support'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('package/', views.package, name='package'),
    # pa9th('filter/', views.filter_tours, name='filter_tours'),
    path('search/', search_destinations, name='search_destinations'),
    path ('recommendations/' , filter_destinations, name='filter_destinations'),
    path('personalized/', personalized_recommendations, name='personalized_recommendations'),
    path('favorites/add/<int:destination_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/', view_favorites, name='view_favorites'),
    path('favorites/remove/<int:destination_id>/', views.remove_favorite, name='remove_favorite'),
   

    
]