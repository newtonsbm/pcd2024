# create drf serializers

from rest_framework import serializers
from padarias import models


class CestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cesta
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = '__all__'