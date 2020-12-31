import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):

    ticket_num = CharFilter(label='Ticket Number', lookup_expr="icontains")
    order_num = CharFilter(label='Order Number', lookup_expr="icontains")

    class Meta:
        model = Order
        fields = ['ticket_num','order_num', 'kitchen']