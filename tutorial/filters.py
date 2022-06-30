from itertools import product
from django.db import models
import django_filters as filters

from tutorial.models import Person


class PersonFilter(filters.FilterSet):
    name = filters.ModelMultipleChoiceFilter(queryset=Person.objects.all())
    