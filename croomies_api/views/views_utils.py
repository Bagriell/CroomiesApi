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
import json
import datetime
from ..IA.format_data import predict_cluster

class colocation_seekerAPI(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        listMatchings = serializers.serialize("json", Matching.objects.all()),
        return HttpResponse(listMatchings)

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)

        #addressSplitted = data["data"]["address"]["city"].split(",")
        #print(addressSplitted[1]) #city + postcode
        #postcode = [int(i) for i in addressSplitted[1].split() if i.isdigit()]
        #city = ''.join([j for j in addressSplitted[1] if not j.isdigit()])
        #country= "France" #en dur pour le moment
        #street= addressSplitted[0]
        #dateBegin = datetime.datetime.strptime(data["data"]["date"]["begin"], "%d/%m/%Y").strftime("%Y-%m-%d")
        #print(dateBegin)

        #* add password rules ?

        isValidDateBegin = True
        month,day,year = data["data"]["date"]["begin"].split('/')# format du front MM/DD/YYYY
        try :
            datetime.datetime(int(year),int(month),int(day))
        except ValueError :
            isValidDateBegin = False

        if(isValidDateBegin == False) :
            print ("Input Begining date is not valid..")
            return Response("Input Begining date is not valid.." , status=status.HTTP_400_BAD_REQUEST)

        new_case_dateYYYYMMDDbegin = year+"-"+month+"-"+day

        isValidDateEnd = True
        month,day,year = data["data"]["date"]["end"].split('/')
        try :
            datetime.datetime(int(year),int(month),int(day))
        except ValueError :
            isValidDateEnd = False

        if(isValidDateEnd == False) :
            print ("Input ending date is not valid..")
            return Response("Input Ending date is not valid.." , status=status.HTTP_400_BAD_REQUEST)

        new_case_dateYYYYMMDDend = year+"-"+month+"-"+day
        datajson = json.dumps(data["data"])
        id_cluster = predict_cluster(datajson)
        print("CLUSTER: ", id_cluster)
        CroomiesUser.objects.create(first_name=data["data"]["first_name"], last_name=data["data"]["last_name"], password=data["data"]["password"], age=data["data"]["profile"]["age"], activity=data["data"]["profile"]["activity"], gender=data["data"]["profile"]["gender"], phone_number=data["data"]["profile"]["phone_number"], diet=data["data"]["answers"]["diet"], drinks=data["data"]["answers"]["drinks"], education=data["data"]["answers"]["education"], pets=data["data"]["answers"]["pets"], speaks=data["data"]["answers"]["speaks"], religion=data["data"]["answers"]["religion"], smokes=data["data"]["answers"]["smokes"])
        Address.objects.create(city=data["data"]["address"]["city"], country=data["data"]["address"]["country"], address=data["data"]["address"]["street"], postcode=data["data"]["address"]["postcode"])
        Seeker.objects.create(id_user= CroomiesUser.objects.get(first_name= data["data"]["first_name"], last_name=data["data"]["last_name"], password= data["data"]["password"]), budget_min= data["data"]["budget"]["min"], budget_max= data["data"]["budget"]["max"], number_of_room= data["data"]["numberSeeker"]["numberOfRoom"], is_empty_habitation= data["data"]["numberSeeker"]["emptyHabitation"], searching_from= new_case_dateYYYYMMDDbegin, searching_to= new_case_dateYYYYMMDDend)
        return Response("Created", status=status.HTTP_201_CREATED)