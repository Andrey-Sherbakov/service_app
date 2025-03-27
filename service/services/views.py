from django.shortcuts import render
from rest_framework import viewsets

from services.models import Subscription
from services.serializers import SubscriptionSerializer


class SubscriptionView(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().select_related('client', 'client__user', 'plan').only(
        'client__user__email',
        'client__company_name',
        'plan_id'
    )
    serializer_class = SubscriptionSerializer
