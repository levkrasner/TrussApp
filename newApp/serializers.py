from django.contrib.auth.models import User, Group
from rest_framework import serializers

from newApp.models import Tenant


class TenantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = ('first_name', 'last_name')


