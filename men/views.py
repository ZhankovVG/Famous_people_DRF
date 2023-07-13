from rest_framework import viewsets, generics
from .models import Men
from .serializers import MenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination


# class MenViewSet(viewsets.ModelViewSet):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


class MenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 1000
    

class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MenAPIListPagination
    

class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated, )
    
    
class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly, )