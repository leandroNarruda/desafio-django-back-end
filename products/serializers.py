from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    code = serializers.CharField()
    category = serializers.CharField()
    provider = serializers.CharField()
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
