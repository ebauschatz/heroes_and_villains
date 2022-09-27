from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer


@api_view(['GET'])
def super_by_id(request, pk):
    found_super = get_object_or_404(Super, pk = pk)
    if request.method == 'GET':
        serializer = SuperSerializer(found_super)
        return Response(serializer.data, status=status.HTTP_200_OK)