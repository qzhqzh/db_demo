from rest_framework import routers
from core.views import *

routers = routers.SimpleRouter(trailing_slash=False)

routers.register('primer', PrimerViewSet)

urlpatterns = routers.urls