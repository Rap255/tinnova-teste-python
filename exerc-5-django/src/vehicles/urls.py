from django.urls import path
from vehicles import views

urlpatterns = [
    path('', views.VehiclesView.as_view()),
    path('<int:vehicle_id>', views.VehicleView.as_view()),
]