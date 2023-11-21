from rest_framework import viewsets
from .models import Cat
from .serializers import CatSerializer
from rest_framework.permissions import IsAuthenticated

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(breeder=self.request.user)