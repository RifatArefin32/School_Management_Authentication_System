# apps/users/urls.py

from django.urls import path
from .views import StudentRegisterView

urlpatterns = [
    # students
    path('student/register/', StudentRegisterView.as_view(), name='student-register'),
]
