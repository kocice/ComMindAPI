from django.db import models


class Product(models.Model):
    product_business_key = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    product_url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=500, blank=True)
    product_rating = models.FloatField(blank=True, null=True)
    nb_reviewers = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProductRemark(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
    )
    remark = models.TextField()
    date = models.DateField()
    region = models.CharField(max_length=50)
    keyword = models.TextField()
    topic_perc_contrib = models.FloatField()
    dominant_topic = models.IntegerField(blank=True, null=True)
    polarity = models.FloatField(blank=True, null=True)
    subjectivity = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.region

# Récupérer l'id du produit
# - Récupérer le nombre total de commentaires liés au produit
# - Récupérer les sujets dominant pour chaque commentaire du produit
# - Récupérer le pourcentage d'apparition de chaque sujet
# - Récupérer le pourcentage du sujet dominant
# - Récupérer les mots clés liés au sujet

