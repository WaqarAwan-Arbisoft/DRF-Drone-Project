from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
from drones.serializers import DroneCategorySerializer
from drones.serializers import DroneSerializer
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer
from rest_framework.response import Response

from rest_framework import filters
from django_filters import AllValuesFilter,DateTimeFilter,NumberFilter

from rest_framework import permissions
from . import customPermissions


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'

    filter_fields=(
        'name',
    )
    search_fields=(
        '^name',#^ shows that it will search for the string that starts with our name search
    )

    ordering_fields=(
        'name',
    )


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'
    
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'

    filter_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        'manufacturing_date',
        )

    permission_classes=(permissions.IsAuthenticatedOrReadOnly,customPermissions.isCurrentUserOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'

    permission_classes=(permissions.IsAuthenticatedOrReadOnly ,customPermissions.isCurrentUserOwnerOrReadOnly)


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'

    filter_fields = (
        'name',
        'gender',
        'races_count',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        'races_count'
        )
    permission_classes=(permissions.IsAuthenticated,)
class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

    permission_classes=(permissions.IsAuthenticated,)

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'



# Not good understanding
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
            })