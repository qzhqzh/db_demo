from rest_framework.serializers import ModelSerializer
from core.models import Primer

class PrimerSerializer(ModelSerializer):
    class Meta:
        model = Primer
        fields = '__all__'