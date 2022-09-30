from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from super_types.models import SuperType
from powers.models import Power


@api_view(['GET', 'PUT', 'DELETE'])
def super_by_id(request, pk):
    found_super = get_object_or_404(Super, pk = pk)
    if request.method == 'GET':
        serializer = SuperSerializer(found_super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SuperSerializer(found_super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        found_super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def supers_list(request):
    if request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        super_type_param = request.query_params.get('type')
        if super_type_param:
            supers = Super.objects.filter(super_type__type = super_type_param)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            custom_response = {}
            super_types = SuperType.objects.all()
            supers = Super.objects.all()
            for current_type in super_types:
                supers_of_type = supers.filter(super_type = current_type.id)
                serializer = SuperSerializer(supers_of_type, many=True)
                custom_response[current_type.type] = serializer.data
            return Response(custom_response, status=status.HTTP_200_OK)
        
@api_view(['PATCH'])
def add_power_to_super(request, super_pk, power_pk):
    super = get_object_or_404(Super, pk = super_pk)
    power = get_object_or_404(Power, pk = power_pk)
    super.powers.add(power)
    serializer = SuperSerializer(super)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def super_battle(request):
    hero_param = request.query_params.get('hero_name')
    hero = get_object_or_404(Super, name = hero_param)    
    hero_serializer = SuperSerializer(hero)
    villain_param = request.query_params.get('villain_name')
    villain = get_object_or_404(Super, name = villain_param)
    villain_serializer = SuperSerializer(villain)
    custom_response = {}
    if hero.powers.count() > villain.powers.count():
        custom_response['winner'] = hero_serializer.data
        custom_response['loser'] = villain_serializer.data
        return Response(custom_response, status=status.HTTP_200_OK)
    elif hero.powers.count() < villain.powers.count():
        custom_response['winner'] = villain_serializer.data
        custom_response['loser'] = hero_serializer.data
        return Response(custom_response, status=status.HTTP_200_OK)
    else:
        custom_response['tied'] = [hero_serializer.data, villain_serializer.data]
        return Response(custom_response, status=status.HTTP_200_OK)

@api_view(['GET'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk = pk)
    return render(request, 'super_detail.html', {'super': super})