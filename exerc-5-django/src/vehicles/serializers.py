from rest_framework import serializers, exceptions
from vehicles.models import Vehicles

class VehicleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = (
            "veiculo",
            "marca",
            "ano",
            "descricao",
            "vendido"
        )

class VehicleRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = "__all__"