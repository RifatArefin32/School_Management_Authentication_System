# apps/users/urls.py

from django.urls import path
from .views import StudentRegisterView

urlpatterns = [
    path('api/student/register/', StudentRegisterView.as_view(), name='student-register'),
]
