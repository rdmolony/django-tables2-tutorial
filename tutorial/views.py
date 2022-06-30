from django_tables2 import SingleTableView

from tutorial.models import Person
from tutorial.tables import PersonTable

class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'
