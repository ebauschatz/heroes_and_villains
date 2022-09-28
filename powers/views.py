from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Power
from .serializers import PowerSerializer

@api_view(['GET', 'POST'])
def powers_list(request):
    if request.method == 'GET':
        powers = Power.objects.all()
        serializer = PowerSerializer(powers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PowerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)