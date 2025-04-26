from rest_framework import generics
from .serializers import StudentRegistrationSerializer
from apps.users.models import SchoolUser

class StudentRegisterView(generics.CreateAPIView):
    queryset = SchoolUser.objects.all()
    serializer_class = StudentRegistrationSerializer
