from django.db.models import Q
from django_filters import rest_framework as filters

from products.models import Product


class ProductFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_value',label='Search')
    cost = filters.NumberFilter(field_name='cost', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ('search', 'cost')

    def filter_by_value(self, queryset, name, value):
        filter_params = Q()
        if self.request.query_params['search']:
            list_of_words = list(map(str, self.request.query_params['search'].split()))
            for word in list_of_words:
                filter_params |= Q(name__contains=word)
                filter_params |= Q(description_contains=word)
        result = queryset.filter(filter_params)
        return result