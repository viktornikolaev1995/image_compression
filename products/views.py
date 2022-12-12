from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from products import serializers
from products.models import Product


PRODUCT_QUERY_PARAMS = [
    openapi.Parameter('name', openapi.IN_QUERY, description='Название', type=openapi.TYPE_ARRAY,
                      items=openapi.Items(type=openapi.TYPE_STRING), collection_format='multi', required=False),
    openapi.Parameter('article', openapi.IN_QUERY, description='Артикул', type=openapi.TYPE_ARRAY,
                      items=openapi.Items(type=openapi.TYPE_STRING), collection_format='multi', required=False),
    openapi.Parameter('status', openapi.IN_QUERY, description='Статус', type=openapi.TYPE_ARRAY,
                      items=openapi.Items(type=openapi.TYPE_STRING), collection_format='multi', required=False),
]


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=['products/'],
    manual_parameters=PRODUCT_QUERY_PARAMS,
    operation_id='product_list',
    operation_summary='Список всех товаров',
    responses={
        status.HTTP_200_OK: openapi.Response(
            description='Список всех товаров',
            schema=serializers.ProductSerializer(many=True),
        )
    }
))
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.select_related('image').all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = dict(self.request.query_params)
        filters = Q()
        for param, values in query_params.items():
            filters &= Q(**{f"{param}__in": values})

        return queryset.filter(filters)


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=['products/'],
    operation_id='product_retrieve',
    operation_summary='Просмотр информации о товаре',
    responses={
        status.HTTP_200_OK: openapi.Response(
            description='Просмотр информации о товаре',
            schema=serializers.ProductSerializer(many=True),
        )
    }
))
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('image').all()
    serializer_class = serializers.ProductSerializer
