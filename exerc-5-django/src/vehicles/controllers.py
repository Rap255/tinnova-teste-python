from vehicles.models import Vehicles
from rest_framework.generics import ListAPIView
from vehicles.serializers import (
    VehicleCreateSerializer,
    VehicleRetrieveSerializer
)
from rest_framework.response import Response
from rest_framework import status
from services.utils import paginator
from services.utils import form_formatter
from datetime import datetime


model = Vehicles

class VehiclesController(ListAPIView):

    model = Vehicles
    serializer_list = VehicleCreateSerializer

    @classmethod
    def create_vehicle(cls,request):
        serializer = VehicleCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            payload = serializer.data
            return model.objects.create(**payload)
        else:
            return Response(
                data={"message": "an error has occured"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    @staticmethod
    def list_vehicle_by_id(request,vehicle_id):
        vehicle = model.objects.get(id=vehicle_id)
        return VehicleRetrieveSerializer(vehicle).data
    
    @staticmethod
    def list_vehicles(request, per_page=20):
        query_params = form_formatter(request.query_params)
        filter_page = {}

        if 'vendido' in query_params:
            if query_params['vendido'] == "true" or query_params['vendido'] == "True":
                query_params["vendido"] == True
            else:
                query_params["vendido"] == False

        if 'per_page' in query_params:
            filter_page['per_page'] = query_params['per_page']
            del query_params['per_page']
        
        if 'page' in query_params:
            filter_page['page'] = query_params['page']
            del query_params['page']
        
        vehicles_objs = model.objects.filter(**query_params).order_by('id')
        return paginator(vehicles_objs,"vehicles",VehicleRetrieveSerializer,**filter_page)
    
    @classmethod
    def edit_vehicle(cls,id_vehicle,request,method="PUT"):

        if method == 'PUT':
            list_filds = ['veiculo','marca','ano','descricao','vendido']
            for key in list_filds:
                if key not in request.data:
                    print('aq')
                    return False
            
        form = request.data
        vehicle_obj = cls.model.objects.get(id=id_vehicle)
        vehicle_obj.updated = str(datetime.now())
        for key,value in form.items():
            setattr(vehicle_obj,key,value)
        vehicle_obj.save()
        
        return vehicle_obj

    @classmethod
    def delete_vehicle(cls,id):
        if vehicle_obj := model.objects.get(id=id):
            vehicle_obj.delete()
            return True
        else:
            return False