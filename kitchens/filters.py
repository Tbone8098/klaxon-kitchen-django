import django_filters
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):

    order_num = django_filters.CharFilter(label='Order Number')

    class Meta:
        model = Order
        fields = ['order_num', 'kitchen']