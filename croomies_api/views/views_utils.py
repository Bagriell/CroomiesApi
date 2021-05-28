from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.serializers import Serializer
from ..models import Address, Habitation, Sport, Film, Music, Sport_user, Film_user, Music_user, Media, CroomiesUser, Seeker, Matching, Roomate_in_habitation, Media_habitation, Time_slots, Date_slots, Visite, Application
from rest_framework.response import Response
from knox.models import AuthToken
from ..serializers import UserSerializer, RegisterSerializer, AddressSerializer,HabitationSerializer, SportSerializer, FilmSerializer, MusicSerializer, Sport_userSerializer, Film_userSerializer, Music_userSerializer, MediaSerializer, SeekerSerializer, MatchingSerializer, Roomate_in_habitationSerializer, Media_habitationSerializer, CroomiesUserSerializer, Time_slotsSerializer, Date_slotsSerializer, VisiteSerializer, ApplicationSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import HttpResponse
from django.core import serializers
from rest_framework import status

class colocation_seekerAPI(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        listMatchings = serializers.serialize("json", Matching.objects.all()),
        return HttpResponse(listMatchings)

    def post(self, request, *args, **kwargs):
        try:
            CroomiesUser.objects.create(first_name=request.data["first_name"], last_name=request.data["last_name"], password=request.data["password"], age=request.data["profile"]["age"], activity=request.data["profile"]["activity"], gender=request.data["profile"]["gender"], phone_number=request.data["profile"]["phone_number"], diet=request.data["answers"]["diet"], drinks=request.data["answers"]["drinks"], drugs=request.data["answers"]["drugs"], education=request.data["answers"]["education"], pets=request.data["answers"]["pets"], speaks=request.data["answers"]["speaks"], religion=request.data["answers"]["religion"], smokes=request.data["answers"]["smokes"])
            Address.objects.create(city=request.data["address"]["city"], country=request.data["address"]["country"], address=request.data["address"]["street"], postcode=request.data["address"]["postcode"])
            Seeker.objects.create(id_user= CroomiesUser.objects.get(first_name= request.data["first_name"], last_name=request.data["last_name"], password= request.data["password"]), budget_min= request.data["budget"]["min"], budget_max= request.data["budget"]["max"], number_of_room= request.data["numberSeeker"]["numberOfRoom"], is_empty_habitation= request.data["numberSeeker"]["emptyHabitation"], searching_from= request.data["date"]["begin"], searching_to= request.data["date"]["end"])
            return Response("Created", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response("Error" , status=status.HTTP_400_BAD_REQUEST)