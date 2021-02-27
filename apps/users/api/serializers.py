from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self,value):
        # Costom validation
        if 'developer' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        
        return value

    def validate_email(self,value):
        if value == '':
            raise serializers.ValidationError('Tiene que ingresar un correo')

        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('el email no puede contener el nombre')
        return value

    def validate(self,data):
        # if data['name'] in data['email']:
        #     raise serializers.ValidationError('el email no puede contener el nombre')
        return data

    def create(self,validate_data):
        print(validate_data)
        return User.objects.create(**validate_data)