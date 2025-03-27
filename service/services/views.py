from django.db.models import F, Sum
from django.shortcuts import render
from rest_framework import viewsets

from services.models import Subscription
from services.serializers import SubscriptionSerializer


class SubscriptionView(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().select_related('client', 'client__user', 'plan').only(
        'client__user__email',
        'client__company_name',
        'plan_id',
    ).annotate(price=F('service__full_price') -
                       F('service__full_price') * F('plan__discount_percent') / 100.00)
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).aggregate(total_amount=Sum('price'))

        response = super().list(request, *args, **kwargs)

        response_data = {'total_amount': queryset['total_amount'],
                         'subscriptions': response.data}
        response.data = response_data
        return response

