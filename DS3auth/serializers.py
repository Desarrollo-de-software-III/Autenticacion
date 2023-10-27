from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Crea un nuevo usuario utilizando el modelo personalizado de usuario
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        if not email or not password:
            raise serializers.ValidationError('El correo electrónico y la contraseña son obligatorios.')

        user = User.objects.create_user(email=email, password=password)
        return user
