from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer

@api_view(['GET','POST'])
def user_api_view(request):

    # List
    if request.method == 'GET':
        # Consulta
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        test_data = {
            'name': 'develop',
            'email': 'testp@gmail.com'
        }
        test_user = TestUserSerializer(data = test_data, context=test_data)
        if test_user.is_valid():
            user_instance = test_user.save()
            print(user_instance.id)
        else:
            print(test_user.errors)
        
        return Response(users_serializer.data)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        
        return Response(user_serializer.errors)


@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    # Consulta
    user = User.objects.filter(id = pk).first()
    # Validacion
    if user:

        # Retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        
        # Update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)

            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)

            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':     
            user.delete()
            return Response({'message':'Usuario eliminado correctamente!'},status = status.HTTP_200_OK)

    return Response({'message':'Usuario no encontrado!'},status = status.HTTP_400_BAD_REQUEST)