from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from service.tasks import set_price, set_comment
from services.models import Subscription


@receiver(post_save, sender=Subscription)
def subscription_pre_save(sender, instance, created, **kwargs):
    if created:
        set_price.delay(instance.pk)
        set_comment.delay(instance.pk)

@receiver(post_delete, sender=Subscription)
def subscription_delete(sender, instance, **kwargs):
    print('subscription_delete')
    cache.delete(settings.TOTAL_CACHE_NAME)