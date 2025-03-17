from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Shop
        fields = ["id", "name", "owner", "type_of_business", "latitude", "longitude"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
