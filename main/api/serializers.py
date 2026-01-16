from django.contrib.auth import authenticate
from rest_framework import serializers #Utilizado no DRF para validar dados, normalizar inputs e controlar dados


#Nosso Serializer Que valida o login, serve exclusivamente para a entrada do usuário na plataforma
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField() #Verifica automaticamente se é do tipo e-mail, se não for da erro 400 automáticamente
    password = serializers.CharField(write_only=True) #O write_only serve para proteção do dado, ele nunca aparecerá na resposta para o usuário

    def validate(self, data): #Após a validação básica, ele recebe todos os campos juntos
        
        #o authenticate procura um usuário e compara o hash da senha
        user = authenticate( #Utilizamos o authenticate para verificar as credenciais
            email=data["email"],
            password=data["password"]
        )

        #Se der erro na autenticação de cima, na comparação, cai aqui
        if not user:
            raise serializers.ValidationError("Login ou senha incorretos")

        data["user"] = user
        return data
