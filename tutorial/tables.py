import django_tables2 as tables

from tutorial.models import Person


class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )
        