from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']

    def to_representation(self, instance):
        return {
            "Nome": instance.nome,
            "Email": instance.email
        }