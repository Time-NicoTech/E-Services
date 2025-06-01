from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from api.serializers import ServiceSerializer
from api.models import Servico
modelo_usuario = get_user_model()

@api_view(['GET'])
def getAllServices(request):
    services = Servico.objects.all()

    servicesJson = ServiceSerializer(services, many=True)

    if services:
        return Response({"Usuarios":servicesJson.data}, status=status.HTTP_200_OK)
    else:
        return Response({"Usuarios":"Nenhum serviço cadastrado"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def addService(request):
    if request.method == 'POST':
        service = ServiceSerializer(data=request.data)

        if service.is_valid():
            service.save()
            return Response({'message':'Serviço cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'message':'Erro no cadastro!', 'errors':service.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': "Método não permitido! Só POST é possível.", 'status':'error'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 