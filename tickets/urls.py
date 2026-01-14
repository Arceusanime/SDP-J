from django.urls import path
from . import views

urlpatterns = [
    path('', views.race_list, name='race_list'),
    path('race/<int:race_id>/', views.ticket_list, name='ticket_list'),
    path('book/<int:ticket_id>/', views.book_ticket, name='book_ticket'),
    path('success/<int:ticket_id>/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('race-detail/<int:race_id>/', views.race_detail, name='race_detail'),
    path("signup/", views.signup_view, name="signup"),
    
]
