from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, EmailField, FloatField, IntegerField, TextField, URLField, DateField, TimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from knox.models import User
from datetime import date

#* Mindmap : https://www.mindmeister.com/fr/1814486318?t=YE8gxhCFsd
#* Excel : https://docs.google.com/spreadsheets/d/1gWNZsbPm08ZI8Q9swAmLyaOUvMjZoWLdwzVbLjHXdkU/edit#gid=0

#TODO Chantier: prevoir upload/photo/video/type de document != de doc officiels

date = models.DateTimeField(auto_now_add=True, blank=True)


class Media(Model):
    url = URLField()
    type_of = CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.url)

class CroomiesUser(Model):
    cluster = IntegerField(blank=True, null=True)
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    is_owner = BooleanField(default=False)
    is_seeker = BooleanField(default=False)
    description = TextField(blank=True, null=True)
    email = EmailField()
    password = CharField(max_length=20)
    is_media = BooleanField(default=False)
    id_media = ForeignKey(Media, on_delete=CASCADE, blank=True, null=True)
    identity_card = URLField(blank=True, null=True)
    student_card = URLField(blank=True, null=True)
    proof_address_self = URLField(blank=True, null=True)
    proof_address_guarantor = URLField(blank=True, null=True)
    identity_card_guarantor = URLField(blank=True, null=True)
    proof_income_self = URLField(blank=True, null=True)
    proof_income_guarantor = URLField(blank=True, null=True)
    tax_notice_self = URLField(blank=True, null=True)
    tax_notice_guarantor = URLField(blank=True, null=True)
    property_tax_guarantor = URLField(blank=True, null=True)
    apl_certificate = URLField(blank=True, null=True)
    nbr_rooms = IntegerField(blank=True, null=True)
    is_whole_habitation = BooleanField(default=False)
    age = IntegerField(blank=True, null=True)
    activity = CharField(max_length=100, blank=True, null=True)
    gender = CharField(max_length=100, blank=True, null=True)
    phone_number = CharField(max_length=20, blank=True, null=True)
    diet = CharField(max_length=100, blank=True, null=True)
    drinks = CharField(max_length=100, blank=True, null=True)
    education = CharField(max_length=100, blank=True, null=True)
    pets = CharField(max_length=100, blank=True, null=True)
    speaks = CharField(max_length=100, blank=True, null=True)
    religion = CharField(max_length=100, blank=True, null=True)
    smokes = CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Address(Model):
    city = CharField(max_length=20)
    country = CharField(max_length=20)
    address = TextField(blank=True, null=True)  # A modifier
    postcode = IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.city, self.address)

class Time_slots(Model):
    hour = TimeField()

class Date_slots(Model):
    date = DateField()

class Habitation(Model):
    title = CharField(max_length=20)
    rooms_nb = IntegerField()
    area = IntegerField()
    id_address = OneToOneField(Address, on_delete=CASCADE, blank=True, null=True)    # Shop-django / Django-address package
    description = TextField()
    compatibility_score = FloatField()
    is_furnished = BooleanField()
    price = IntegerField()
    id_user_poster = ForeignKey(CroomiesUser, on_delete=CASCADE, blank=True, null=True) #il s'agit du gars qui met l'annonce #! remove blank=true et null=true
    id_time_slots = ForeignKey(Time_slots, on_delete=CASCADE, blank=True, null=True)
    id_date_slots =  ForeignKey(Date_slots, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.title, self.description)

class Sport(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.name)

class Film(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.name)

class Music(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Music_user(Model):
    id_music = ManyToManyField(Music)
    id_user = ManyToManyField(CroomiesUser)

    def __str__(self):
        return "%s %s" % (self.id_music, self.id_user)

class Film_user(Model):
    id_film = ManyToManyField(Film)
    id_user = ManyToManyField(CroomiesUser)

    def __str__(self):
        return "%s %s" % (self.id_film, self.id_user)

class Sport_user(Model):
    id_sport = ManyToManyField(Sport)
    id_user = ManyToManyField(CroomiesUser)

    def __str__(self):
        return "%s %s" % (self.id_sport, self.id_user)


class Seeker(Model):
    id_user = ForeignKey(CroomiesUser, on_delete=CASCADE, blank=True, null=True)
    id_adress_search = OneToOneField(Address, on_delete=CASCADE, blank=True, null=True)
    budget_min = IntegerField(blank=True, null=True)
    budget_max = IntegerField(blank=True, null=True)
    number_of_room = IntegerField(blank=True, null=True)
    is_empty_habitation = BooleanField(default= False)
    searching_from = DateField(blank=True, null=True)
    searching_to = DateField(blank=True, null=True)
    where_city = CharField(max_length=20, blank=True, null=True)
    where_country = CharField(max_length=20, blank=True, null=True)
    where_address = TextField(blank=True, null=True)  # A modifier
    where_postcode = IntegerField(blank=True, null=True)


    def __str__(self):
        return "%s %s" % (self.id_user, self.id_localisation_search)

class Matching(Model):
    id_user = ForeignKey(CroomiesUser, on_delete=CASCADE)
    id_seeker = ForeignKey(Seeker, on_delete=CASCADE)
    skip = BooleanField(default=False)
    like = BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.id_matcher, self.id_seeker)


class Roomate_in_habitation(Model):
    id_habitation = ForeignKey(Habitation, on_delete=CASCADE)
    id_user = ForeignKey(CroomiesUser, on_delete=CASCADE)

    def __str__(self):
        return "%s %s" % (self.id_habitation, self.id_user)

class Media_habitation(Model):
    id_habitation = ForeignKey(Habitation, on_delete=CASCADE)
    id_media = ManyToManyField(Media)

    def __str__(self):
        return "%s %s" % (self.id_habitation, self.id_media)

class Visite(Model):
    state = BooleanField(default=False)
    id_habitation = ForeignKey(Habitation, on_delete=CASCADE) #id_logement
    date = DateField()
    hour = TimeField()
    id_seeker = ForeignKey(Seeker, on_delete=CASCADE)

class Application(Model):
    id_habitation = ForeignKey(Habitation, on_delete=CASCADE)
    id_user = ForeignKey(CroomiesUser, on_delete=CASCADE)
    message = TextField()
