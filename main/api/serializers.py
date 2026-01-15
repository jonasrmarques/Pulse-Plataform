from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    
    def validate(self, data):
        user = authenticate(
            request=self.context.get("request"),
            email=data["email"],
            password=data["password"]
        )

        
        if not user:
            raise serializers.ValidationError("Login ou Senha Incorretos")
        
        data["user"] = user
        
        return data