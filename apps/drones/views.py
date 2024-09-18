from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from apps.drones.models import DronesCategory
from apps.drones.models import Drone
from apps.drones.models import Pilote
from apps.drones.models import Competition
from apps.drones.serializers import DroneCategorySerializer
from apps.drones.serializers import DroneSerializer
from apps.drones.serializers import PilotSerializer
from apps.drones.serializers import PilotCompetitionSerializer



class DronesCategoryViewSet(viewsets.ModelViewSet):
    queryset = DronesCategory.objects.all()
    serializer_class = DroneCategorySerializer
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"

class PilotList(generics.ListCreateAPIView):
    queryset = Pilote.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"

class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilote.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-detail"
class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "drone-categories": reverse("dronecategory-list", request=request),
                "drones": reverse(DroneList.name, request=request),
                "pilots": reverse(PilotList.name, request=request),
                "competitions": reverse(CompetitionList.name, request=request),
            }
        )