from django.db.models import fields
from rest_framework import serializers
from .models import Address, Habitation, Music, Sport, Film, Sport_user
from django.contrib.auth.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'address', 'country', 'postcode')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password') #description
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class HabitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitation
        fields = ('title', 'area', 'description')

    def create(self):
        habitation = Habitation.objects.create(
            title=['Neverland'],
            area=['67'],
            description=["Moi c'est Manon, je suis étudiante en Communication de la Mode et une place se libère dans ma coloc sur les quais (quai victor augagneur). En ce qui me concerne, je suis quelqu'un de très joyeux et de facile à vivre"])

        habitation.save()

        habitation = Habitation.objects.create(
            title=['Coloc des Lumières'],
            area=['150'],
            description=["Nous postons une annonce car nous cherchons quelqu'un.e à partir de début Juin et pour la durée que tu souhaites, l'idée est tout de même rester au moins 1 an si possible. De plus, nous aurions une préférence pour une personne déjà dans la vie active."])

        habitation.save()

        habitation = Habitation.objects.create(
            title=["L'octogone"],
            area=['50'],
            description=["Jeune infirmière recherche un ou une coloc pour remplacer ma colocataire actuelle qui retourne dans sa ville natale ! Je recherche un profil soigneux (Hygiène douteuse s'abstenir :p ) mais aussi quelqu'un de sympathique pour apprécier les moments de convivialité et qui gravite autour des 25 ans et plus (critère non éliminatoire) ! :p"])

        habitation.save()

        return habitation

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'
        name = serializers.CharField(max_length=200)

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        name = serializers.CharField(max_length=200)

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        name = serializers.CharField(max_length=200)

class Sport_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_user
        fields = ('id_sport', 'id_user')