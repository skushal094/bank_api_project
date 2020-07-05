from rest_framework import serializers
from . import models


class BranchSerializer(serializers.ModelSerializer):
    """
    This serializer class will serialize the branch objects.
    """
    branch_name = serializers.CharField(source='name')
    bank_name = serializers.CharField(source='bank.name')
    city = serializers.CharField(source='location.city')
    district = serializers.CharField(source='location.district')
    state = serializers.CharField(source='location.state')

    class Meta:
        model = models.Branch
        fields = ('id', 'branch_name', 'bank_name', 'address', 'ifsc_code', 'city', 'district', 'state')