from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2 import SingleTableView

from tutorial.filters import PersonFilter
from tutorial.models import Person
from tutorial.tables import PersonTable

class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'


class FilteredPersonListView(SingleTableMixin, FilterView):
    model = Person
    table_class = PersonTable
    template_name = "template.html"
    filterset_class = PersonFilter