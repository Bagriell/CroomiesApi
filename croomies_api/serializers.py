from django.db.models import fields
from rest_framework import serializers
from .models import Address, Habitation, Media, Music, Sport, Film, Sport_user, Film_user, Music_user, CroomiesUser, Seeker, Matching, Roomate_in_habitation, Media_habitation, Time_slots, Date_slots, Visite, Application
from django.contrib.auth.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'address', 'country', 'postcode')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

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
        fields = ('title', 'rooms_nb', 'area', 'id_address', 'description', 'compatibility_score', 'is_furnished', 'price', 'id_user_poster', 'id_time_slots', 'id_date_slots')

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

class Film_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film_user
        fields = ('id_film', 'id_user')

class Music_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_user
        fields = ('id_music', 'id_user')

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('url', 'type_of')

class CroomiesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CroomiesUser
        fields = ('first_name', 'last_name', 'is_owner', 'is_seeker', 'description', 'email', 'password','is_media', 'id_media', 'identity_card', 'student_card', 'proof_address_self', 'proof_address_guarantor', 'identity_card_guarantor', 'proof_income_self', 'proof_income_guarantor', 'tax_notice_self', 'tax_notice_guarantor', 'property_tax_guarantor', 'apl_certificate', 'nbr_rooms', 'is_whole_habitation', 'age', 'activity', 'gender', 'phone_number', 'diet', 'drinks', 'education', 'pets', 'speaks', 'religion', 'smokes')

class SeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker
        fields = ('id_user', 'id_adress_search', 'budget_min', 'budget_max', 'number_of_room', 'is_empty_habitation', 'searching_from', 'searching_to', 'where_city', 'where_country', 'where_address', 'where_postcode')

class MatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matching
        fields = ('id_user', 'id_seeker', 'skip', 'like')

class Roomate_in_habitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roomate_in_habitation
        fields = ('id_habitation', 'id_user')

class Media_habitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media_habitation
        fields = ('id_habitation', 'id_media')

class Time_slotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_slots
        fields = '__all__'

class Date_slotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date_slots
        fields = '__all__'

class VisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visite
        fields = ('state', 'id_habitation', 'date', 'hour', 'id_seeker')

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id_habitation', 'id_user', 'message')