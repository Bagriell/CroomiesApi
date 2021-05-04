from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, EmailField, FloatField, IntegerField, TextField, URLField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Mindmap : https://www.mindmeister.com/fr/1814486318?t=YE8gxhCFsd


DEFAULT_ID = 1

# Chantier: prevoir upload/photo/video/type de document != de doc officiels
class Media(Model):
    url = URLField()

    def __str__(self):
        return "%s" % (self.url)


class Address(Model):
    city = CharField(max_length=20)
    country = CharField(max_length=20)
    address = TextField()  # A modifier
    postcode = IntegerField()

    def __str__(self):
        return "%s %s" % (self.city, self.address)

class Habitation(Model):
    title = CharField(max_length=20)
    rooms_nb = IntegerField()
    area = IntegerField()
    id_address = ForeignKey(Address, on_delete=CASCADE, default=DEFAULT_ID)    # Shop-django / Django-address package
    description = TextField()
    compatibility_score = FloatField()
    is_furnished = BooleanField()


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

class User(Model):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    is_owner = BooleanField(default=False)
    is_seeker = BooleanField(default=False)
    description = TextField()
    email = EmailField()
    password = CharField(max_length=20)
    id_media = ForeignKey(Media, on_delete=CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Music_user(Model):
    id_music = ForeignKey(Music, on_delete=CASCADE, default=DEFAULT_ID)
    id_user = ForeignKey(User, on_delete=CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return "%s %s" % (self.id_music, self.id_user)

class Film_user(Model):
    id_film = ForeignKey(Film, on_delete=CASCADE, default=DEFAULT_ID )
    id_user = ForeignKey(User, on_delete=CASCADE, default=DEFAULT_ID )

    def __str__(self):
        return "%s %s" % (self.id_film, self.id_user)

class User_sport(Model):
    id_sport = ForeignKey(Sport, on_delete=CASCADE, default=DEFAULT_ID)
    id_user = ForeignKey(User, on_delete=CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return "%s %s" % (self.id_sport, self.id_user)


class Seeker(Model):
    id_user = ForeignKey(User, on_delete=CASCADE, default=DEFAULT_ID)
    id_adress_search = ForeignKey(Address, on_delete=CASCADE, default=DEFAULT_ID)
    budget_min = IntegerField()
    budget_max = IntegerField()

    response_one = FloatField()
    response_two = FloatField()
    response_three = FloatField()
    response_four = FloatField()
    response_five = FloatField()

    def __str__(self):
        return "%s %s" % (self.id_user, self.id_localisation_search)

class Matcher(Model):
    id_seeker = ForeignKey(Seeker, on_delete=CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return "%s %s" % (self.id_seeker)

class Matching(Model):
    id_matcher = ForeignKey(Matcher, on_delete=CASCADE, default=DEFAULT_ID)
    id_seeker = ForeignKey(Seeker, on_delete=CASCADE, default=DEFAULT_ID)
    skip = BooleanField(default=False)
    like = BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.id_matcher, self.id_seeker)


class Roomate_in_habitation:
    id_habitation = ForeignKey(Habitation, on_delete=CASCADE, default=DEFAULT_ID)
    id_user = ForeignKey(User, on_delete=CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return "%s %s" % (self.id_habitation, self.id_user)

class Media_habitation:
    id_habitation = ForeignKey(Habitation, on_delete=CASCADE, default=DEFAULT_ID)
    id_media = ForeignKey(Media, on_delete=CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return "%s %s" % (self.id_habitation, self.id_media)
