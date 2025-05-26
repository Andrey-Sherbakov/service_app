from django.conf import settings
from django.core.cache import cache
from django.db.models import Sum
from rest_framework import viewsets

from services.models import Subscription
from services.serializers import SubscriptionSerializer


class SubscriptionView(viewsets.ModelViewSet):
    queryset = Subscription.objects.all().select_related('client', 'client__user', 'plan').only(
        'client__user__email',
        'client__company_name',
        'plan_id',
        'price',
        'comment',
    )
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        total_cache = cache.get(settings.TOTAL_CACHE_NAME)
        if total_cache:
            total_amount = total_cache
        else:
            total_amount = queryset.aggregate(total=Sum('price')).get('total')
            cache.set(settings.TOTAL_CACHE_NAME, total_amount, 60*60)

        response_data = {'total_amount': total_amount, 'subscriptions': response.data}
        response.data = response_data
        return response
