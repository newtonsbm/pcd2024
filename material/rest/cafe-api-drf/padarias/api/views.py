# create drf viewsets for padarias and cestas

from rest_framework import viewsets

from padarias import models
from . import serializers

class CestaViewSet(viewsets.ModelViewSet):
    queryset = models.Cesta.objects.all()   
    serializer_class = serializers.CestaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
