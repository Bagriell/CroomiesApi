from datetime import date
from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.serializers import Serializer
from ..serializers import AddressSerializer
from ..models import Address, Habitation, Sport, Film, Music, Sport_user, Film_user, Music_user, Media, CroomiesUser, Seeker, Matching, Roomate_in_habitation, Media_habitation, Time_slots, Date_slots, Visite, Application
from rest_framework.response import Response
from knox.models import AuthToken
from ..serializers import UserSerializer,RegisterSerializer, HabitationSerializer, SportSerializer, FilmSerializer, MusicSerializer, Sport_userSerializer, Film_userSerializer, Music_userSerializer, MediaSerializer, SeekerSerializer, MatchingSerializer, Roomate_in_habitationSerializer, Media_habitationSerializer, CroomiesUserSerializer, Time_slotsSerializer, Date_slotsSerializer, VisiteSerializer, ApplicationSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import status
from .views_utils import *

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class HabitationAPI(generics.GenericAPIView):
    serializer_class = HabitationSerializer

    def get(self, request, *args, **kwargs):
        listHabitations = serializers.serialize("json", Habitation.objects.all()),
        return HttpResponse(listHabitations)

    def post(self, request, *args, **kwargs):
        serializer = HabitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HabitationById(generics.GenericAPIView):
    def get(self, request, habitation_id):
        #try:
            hab_for_rm = Roomate_in_habitation.objects.filter(id_habitation = habitation_id)
            data = []
            data.append(Habitation.objects.get(pk=habitation_id))
            for elem in hab_for_rm:
                data.append(elem.id_user)

            resp = serializers.serialize("json", data)
            code = 200
            print(resp[0])
        #except Exception as e:
            #resp = "Habitation not found."
            #code = 400
            return HttpResponse(resp,content_type="application/json") #TODO

class HabitationsWithUser(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        #try:
        habList = Habitation.objects.all()
        data = []
        #data.append(Habitation.objects.all())
        for hab in habList:
            data.append(hab.id_user_poster)
            print(hab.id_user_poster)

        resp = serializers.serialize("json", habList)
        return HttpResponse(resp,content_type="application/json")


class HabitationWithFilterGeo(generics.GenericAPIView): #TODO
    def get(self, request, *args, **kwargs):
        #* Filters are : "geo", "prices", "dates"
        #* Geo filter only work with city name (TL:DR = need Google coordinates)
        #try:
            print("Geo")
            print(self.kwargs)
            city = self.kwargs['param']
            data = Habitation.objects.filter(id_address__city = city)
            resp = serializers.serialize("json", data)
            return HttpResponse(resp,content_type="application/json")

class HabitationWithFilterPrices(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        #* Filters are : "geo", "prices", "dates"
        #try:
            print("Prices")
            print(self.kwargs)
            priceMin = self.kwargs['priceMin']
            priceMax = self.kwargs['priceMax']
            data = Habitation.objects.filter(price__gte = priceMin, price__lte = priceMax)
            resp = serializers.serialize("json", data)
            return HttpResponse(resp,content_type="application/json")

class HabitationWithFilterDates(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        #* Filters are : "geo", "prices", "dates"
        #try:
            print("Dates")
            print(self.kwargs)
            dateBegin = self.kwargs['datebegin'] #* date format YYYY-MM-DD
            dateEnding = self.kwargs['dateending']

            data = Habitation.objects.filter(id_date_slots__date__gte = dateBegin, id_date_slots__date__lte = dateEnding)

            resp = serializers.serialize("json", data)
            return HttpResponse(resp,content_type="application/json") #TODO

class SportAPI(generics.GenericAPIView):
    serializer_class = SportSerializer

    def get(self, request, *args, **kwargs):
        listSports = serializers.serialize("json", Sport.objects.all()),
        return HttpResponse(listSports)

    def post(self, request, *args, **kwargs):
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmAPI(generics.GenericAPIView):
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        listFilms = serializers.serialize("json", Film.objects.all()),
        return HttpResponse(listFilms)

    def post(self, request, *args, **kwargs):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicAPI(generics.GenericAPIView):
    serializer_class = MusicSerializer

    def get(self, request, *args, **kwargs):
        listMusics = serializers.serialize("json", Music.objects.all()),
        return HttpResponse(listMusics)

    def post(self, request, *args, **kwargs):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sport_userAPI(generics.GenericAPIView):
    serializer_class = Sport_userSerializer

    def get(self, request, *args, **kwargs):
        listSport_users = serializers.serialize("json", Sport_user.objects.all()),
        return HttpResponse(listSport_users)

    def post(self, request, *args, **kwargs):
        serializer = Sport_userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Film_userAPI(generics.GenericAPIView):
    serializer_class = Film_userSerializer

    def get(self, request, *args, **kwargs):
        listFilm_users = serializers.serialize("json", Film_user.objects.all()),
        return HttpResponse(listFilm_users)

    def post(self, request, *args, **kwargs):
        serializer = Film_userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Music_userAPI(generics.GenericAPIView):
    serializer_class = Music_userSerializer

    def get(self, request, *args, **kwargs):
        listMusic_users = serializers.serialize("json", Music_user.objects.all()),
        return HttpResponse(listMusic_users)

    def post(self, request, *args, **kwargs):
        serializer = Music_userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaAPI(generics.GenericAPIView):
    serializer_class = MediaSerializer

    def get(self, request, *args, **kwargs):
        listMedias = serializers.serialize("json", Media.objects.all()),
        return HttpResponse(listMedias)

    def post(self, request, *args, **kwargs):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressAPI(generics.GenericAPIView):
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        listAddress = serializers.serialize("json", Address.objects.all()),
        return HttpResponse(listAddress)

    def post(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CroomiesUserAPI(generics.GenericAPIView):
    serializer_class = CroomiesUserSerializer

    def get(self, request, *args, **kwargs):
        listCroomiesUsers = serializers.serialize("json", CroomiesUser.objects.all()),
        return HttpResponse(listCroomiesUsers)

    def post(self, request, *args, **kwargs):
        serializer = CroomiesUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CroomieUserById(generics.GenericAPIView):
    def get(self, request, croomieuser_id):
        try:
            rm_in_hab = Roomate_in_habitation.objects.filter(id_user = croomieuser_id)
            data = []
            data.append(CroomiesUser.objects.get(pk=croomieuser_id))
            for elem in rm_in_hab:
                data.append(elem.id_habitation)

            resp = serializers.serialize("json", data)
            code = 200
        except Exception as e:
            resp = "CroomiesUser not found."
            code = 400
        return Response(resp, code)

class SeekerAPI(generics.GenericAPIView):
    serializer_class = SeekerSerializer

    def get(self, request, *args, **kwargs):
        listSeekers = serializers.serialize("json", Seeker.objects.all()),
        return HttpResponse(listSeekers)

    def post(self, request, *args, **kwargs):
        serializer = SeekerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchingAPI(generics.GenericAPIView):
    serializer_class = MatchingSerializer

    def get(self, request, *args, **kwargs):
        listMatchings = serializers.serialize("json", Matching.objects.all()),
        return HttpResponse(listMatchings)

    def post(self, request, *args, **kwargs):
        serializer = MatchingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Roomate_in_habitationAPI(generics.GenericAPIView):
    serializer_class = Roomate_in_habitationSerializer

    def get(self, request, *args, **kwargs):
        listRoomate_in_habitations = serializers.serialize("json", Roomate_in_habitation.objects.all()),
        return HttpResponse(listRoomate_in_habitations)

    def post(self, request, *args, **kwargs):
        serializer = Roomate_in_habitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Media_habitationAPI(generics.GenericAPIView):
    serializer_class = Media_habitationSerializer

    def get(self, request, *args, **kwargs):
        listMedia_habitations = serializers.serialize("json", Media_habitation.objects.all()),
        return HttpResponse(listMedia_habitations)

    def post(self, request, *args, **kwargs):
        serializer = Media_habitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Time_slotsAPI(generics.GenericAPIView):
    serializer_class = Time_slotsSerializer

    #def get(self, request, *args, **kwargs):
    #    listTime_slots = serializers.serialize("json", Time_slots.objects.all()),
    #    return HttpResponse(listTime_slots)

    def post(self, request, *args, **kwargs):
        serializer = Time_slotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Date_slotsAPI(generics.GenericAPIView):
    serializer_class = Date_slotsSerializer

    def get(self, request, *args, **kwargs):
        listDate_slots = serializers.serialize("json", Date_slots.objects.all()),
        return HttpResponse(listDate_slots)

    def post(self, request, *args, **kwargs):
        serializer = Date_slotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisiteAPI(generics.GenericAPIView):
    serializer_class = VisiteSerializer

    def get(self, request, *args, **kwargs):
        listVisites = serializers.serialize("json", Visite.objects.all()),
        return HttpResponse(listVisites)

    def post(self, request, *args, **kwargs):
        serializer = VisiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationAPI(generics.GenericAPIView):
    serializer_class = ApplicationSerializer

    def get(self, request, *args, **kwargs):
        listApplications = serializers.serialize("json", Application.objects.all()),
        return HttpResponse(listApplications)

    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

