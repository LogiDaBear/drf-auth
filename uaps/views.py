from rest_framework import generics
from .serializer import UAPSSerializer
from .models import UAPS
from .permissions import IsOwnerOrReadOnly


class UAPSList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = UAPS.objects.all()
    serializer_class = UAPSSerializer


class UAPSDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = UAPS.objects.all()
    serializer_class = UAPSSerializer