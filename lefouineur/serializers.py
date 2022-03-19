from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lefouineur.models import Product, ProductRemark


class RemarkSerializer(ModelSerializer):
    class Meta:
        model = ProductRemark
        fields = [
            'id', 'product_id', 'dominant_topic', 'topic_perc_contrib',
            'date', 'region', 'keyword', 'remark', 'polarity', 'subjectivity'
        ]


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'product_url', 'image_url', 'product_rating']


class ProductDetailSerializer(ModelSerializer):
    remarks = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'product_url', 'image_url', 'product_rating',
            'remarks', 'nb_reviewers'
        ]

    def get_remarks(self, instance):
        # Le paramètre 'instance' est l'instance de la catégorie consultée.
        # Dans le cas d'une liste, cette méthode est appelée autant de fois qu'il y a
        # d'entités dans la liste

        # On applique le filtre sur notre queryset pour n'avoir que les produits actifs
        queryset = instance.productremark_set.all()
        # Le serializer est créé avec le queryset défini et toujours défini en tant que many=True
        serializer = RemarkSerializer(queryset, many=True)
        # la propriété '.data' est le rendu de notre serializer que nous retournons ici
        return serializer.data
