from django.urls import path
from .views import login_view, courses_view, assignments_view, register_view

urlpatterns = [
    path('', login_view, name='login'),
    path('courses/', courses_view, name='courses'),
    path('assignments/', assignments_view, name='assignments'),
    path('register/', register_view, name='register'),
]
