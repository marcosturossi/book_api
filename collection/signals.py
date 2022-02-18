from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from.models import Collection


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    """Recebe o sinal quando um novo usuário é criado e cria um token e um collection para ele"""
    if created:
        Token.objects.create(user=instance)
        Collection.objects.create(user=instance)
