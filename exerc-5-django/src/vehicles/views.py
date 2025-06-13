from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from vehicles.serializers import (
    VehicleCreateSerializer,
    VehicleRetrieveSerializer
)
from vehicles.controllers import VehiclesController
from django.db.models import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from services.utils import GetAllow, PostAllow

class VehiclesView(GenericAPIView):

    per_page = openapi.Parameter('per_page', in_=openapi.IN_QUERY,description="Per Page Itens",type=openapi.TYPE_STRING)
    page = openapi.Parameter('page', in_=openapi.IN_QUERY,description="Choose Page",type=openapi.TYPE_STRING)
    marca = openapi.Parameter('marca', in_=openapi.IN_QUERY,description="Vehicle Brand",type=openapi.TYPE_STRING)
    veiculo = openapi.Parameter('veiculo', in_=openapi.IN_QUERY,description="Vehicle Name",type=openapi.TYPE_STRING)
    ano = openapi.Parameter('ano', in_=openapi.IN_QUERY,description="Vehicle Year",type=openapi.TYPE_STRING)
    vendido = openapi.Parameter('vendido', in_=openapi.IN_QUERY,description="Vehicle Status",type=openapi.TYPE_STRING)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return VehicleRetrieveSerializer
        if self.request.method == "POST":
            return VehicleCreateSerializer

    @swagger_auto_schema(operation_id="List Vehicles",manual_parameters=[marca,veiculo,ano,vendido,per_page,page])
    def get(self, request):
        if list_vehicles := VehiclesController.list_vehicles(request):
            return JsonResponse(list_vehicles, status=200)
        else:
            return JsonResponse({"vehicles": []}, status=200)

    @swagger_auto_schema(operation_id='Create Vehicles')
    def post(self, request):
        vehicle_obj = VehiclesController.create_vehicle(request)
        return JsonResponse({"result": "Vehicle created successfully"}, status=201)
    

class VehicleView(GenericAPIView):

    def get_serializer_class(self):
        if self.request.method == "GET":
            return VehicleRetrieveSerializer
    def get_serializer_class(self):
        if self.request.method == "PATCH" or self.request.method == "PUT":
            return VehicleRetrieveSerializer


    @swagger_auto_schema(operation_id="Get Vehicle by Id")
    def get(self, request, vehicle_id):
        try:
            response_controller = VehiclesController.list_vehicle_by_id(request,vehicle_id)
            return JsonResponse({"vehicle": response_controller}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Vehicle does not exist"}, status=404)
    
    @swagger_auto_schema(operation_id="Edit Vehicle by Id")
    def put(self,request,vehicle_id):
        try:
            if response_controller := VehiclesController.edit_vehicle(vehicle_id,request):
                return JsonResponse({"Response": "Vehicle Edit"}, status=200)
            else:
                return JsonResponse({"error": "Parameters Invalid"}, status=400)
        except VehiclesController.model.DoesNotExist:
                return JsonResponse({"error": "Vehicle does not exist"}, status=404)
        
    @swagger_auto_schema(operation_id="Edit Field Vehicle by Id")
    def patch(self,request,vehicle_id):
        try:
            if response_controller := VehiclesController.edit_vehicle(vehicle_id,request,method="PATCH"):
                return JsonResponse({"Response": "Vehicle Edit"}, status=200)
            else:
                return JsonResponse({"error": "Parameters Invalid"}, status=400)
        except VehiclesController.model.DoesNotExist:
                return JsonResponse({"error": "Vehicle does not exist"}, status=404)
    
    @swagger_auto_schema(operation_id='Vehicle Delete')
    def delete(self, request, vehicle_id):
        try:
            user_obj = VehiclesController.delete_vehicle(vehicle_id)
            return JsonResponse({"result": "Vehicle delete successfully"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Vehicle does not exist"}, status=404)
        except:
            return JsonResponse({"error": "Vehicle error deleting"}, status=500)



