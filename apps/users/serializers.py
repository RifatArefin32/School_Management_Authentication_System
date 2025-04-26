# apps/users/serializers.py

from rest_framework import serializers
from apps.users.models import SchoolUser, Student

class StudentRegistrationSerializer(serializers.ModelSerializer):
    roll_number = serializers.CharField(write_only=True)
    study_class = serializers.CharField(write_only=True)
    section = serializers.CharField(write_only=True, required=False, allow_blank=True)
    group = serializers.CharField(write_only=True, required=False, allow_blank=True)
    shift = serializers.CharField(write_only=True, required=False, allow_blank=True)
    session = serializers.CharField(write_only=True, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = SchoolUser
        fields = ('username', 'email', 'phone_number', 'password', 'roll_number', 'study_class', 'section', 'group', 'shift', 'session')

    def create(self, validated_data):
        roll_number = validated_data.pop('roll_number')
        study_class = validated_data.pop('study_class')
        section = validated_data.pop('section', '')
        group = validated_data.pop('group', '')
        shift = validated_data.pop('shift', '')
        session = validated_data.pop('session', '')

        # Create the main user
        user = SchoolUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            user_role='student',  # important: force role as student
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create the student profile
        Student.objects.create(
            user=user,
            roll_number=roll_number,
            study_class=study_class,
            section=section,
            group=group,
            shift=shift,
            session=session,
        )

        return user
