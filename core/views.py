from core.models import Primer
from core.serializers import PrimerSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class PrimerViewSet(ModelViewSet):
    queryset = Primer.objects.all()
    serializer_class = PrimerSerializer