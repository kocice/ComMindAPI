from django.http import HttpResponse
from rest_framework.viewsets import ReadOnlyModelViewSet

from lefouineur.models import Product, ProductRemark
from lefouineur.serializers import RemarkSerializer, ProductDetailSerializer, ProductListSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    # Ajoutons un attribut de classe qui nous permet de définir notre serializer de détail
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_class(self):
        # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class RemarkViewset(ReadOnlyModelViewSet):
    serializer_class = RemarkSerializer

    def get_queryset(self):
        # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = ProductRemark.objects.all()
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        product_id = self.request.GET.get('product_id')
        print(product_id)
        if product_id is not None:
            queryset = queryset.filter(product_id_id=product_id)
        return queryset
