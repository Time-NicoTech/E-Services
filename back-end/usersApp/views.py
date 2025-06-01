from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from api.serializers import UsuarioSerializer
modelo_usuario = get_user_model()

@api_view(['GET'])
def getAllUsers(request):
    users = modelo_usuario.objects.all()

    usersJson = UsuarioSerializer(users, many=True)


    if users:
        return Response({"Usuarios":usersJson.data}, status=status.HTTP_200_OK)
    else:
        return Response({"Usuarios":"Nenhum usuário cadastrado"}, status=status.HTTP_400_BAD_REQUEST)
        





@api_view(['POST'])
def addUser(request):
    if request.method == 'POST':
        user = UsuarioSerializer(data=request.data)

        if user.is_valid():
            user.save()
            print(user)
            return Response({'message':'Usuário cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'message':'Erro no cadastro!', 'errors':user.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': "Método não permitido! Só POST é possível.", 'status':'error'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



