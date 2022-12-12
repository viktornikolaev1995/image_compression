from rest_framework import serializers

from products.models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["path", "formats"]

    def get_path(self, instance):
        return instance.image.url.rsplit(".", 1)[0]


class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)

    class Meta:
        model = Product
        fields = "__all__"
