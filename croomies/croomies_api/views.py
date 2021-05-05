from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.serializers import Serializer
from .serializers import AddressSerializer
from .models import Address, Habitation, Sport, Film, Music
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, HabitationSerializer, SportSerializer, FilmSerializer, MusicSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import HttpResponse
from django.core import serializers
from rest_framework import status




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
        address=Address.objects.create(
            city="Paris",
            country="Fronce",
            address="rue bamboola",
            postcode=223445
        )
        address.save()
        habitation = Habitation.objects.create(
            title=request.POST["title"],
            area=request.POST["area"],
            id_address= address,
            rooms_nb=1,
            compatibility_score=1.20,
            is_furnished=True,
            description="Moi c'est Manon, je suis étudiante en Communication de la Mode et une place se libère dans ma coloc sur les quais (quai victor augagneur). En ce qui me concerne, je suis quelqu'un de très joyeux et de facile à vivre")

        habitation.save()
        print("post post")
        return HttpResponse("reeeee")

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