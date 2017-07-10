from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'key_walmart', 'password',
                  'confirm_password']

        def created(self, data):
            return UserProfile.objects.create(**data)

        def update(self, instance, data):
            instance.username = data.get('username', instance.username)
            instance.key_walmart = data.get('key_walmart', instance.key_walmart)

            instance.save()

            password = data.get('password', None)
            confirm_password = data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance